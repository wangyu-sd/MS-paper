"""Wrap a PNG in a single page without resampling. Requires Pillow and pypdf."""
import argparse
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from PIL import Image, ImageCms
from pypdf import PdfWriter
from pypdf.generic import (
    ArrayObject, BooleanObject, DecodedStreamObject, DictionaryObject, FloatObject,
    NameObject, NumberObject,
)


def add_image(image, color_space):
    stream = DecodedStreamObject()
    stream.set_data(image.tobytes())
    stream.update({
        NameObject("/Type"): NameObject("/XObject"),
        NameObject("/Subtype"): NameObject("/Image"),
        NameObject("/Width"): NumberObject(image.width),
        NameObject("/Height"): NumberObject(image.height),
        NameObject("/ColorSpace"): color_space,
        NameObject("/BitsPerComponent"): NumberObject(8),
        NameObject("/Interpolate"): BooleanObject(False),
    })
    return stream.flate_encode()


def export_png(input_path, output_path, width_mm):
    with Image.open(input_path) as source:
        if source.format != "PNG" or getattr(source, "n_frames", 1) != 1:
            raise ValueError("Expected a single-frame PNG")
        if source.mode not in {"RGB", "RGBA"}:
            raise ValueError("Expected an 8-bit RGB or RGBA PNG")
        rgba = source.convert("RGBA")
        profile = source.info.get("icc_profile")
        if not profile:
            profile = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()

    # A shared points-per-pixel scale preserves the exact decimal page aspect ratio.
    point_scale = (width_mm * Decimal(72) / Decimal("25.4") / rgba.width).quantize(
        Decimal("0.00001"), rounding=ROUND_HALF_UP
    )
    page_width = point_scale * rgba.width
    page_height = point_scale * rgba.height
    pdf = PdfWriter()
    pdf.pdf_header = "%PDF-1.4"
    page = pdf.add_blank_page(float(page_width), float(page_height))
    page.mediabox.upper_right = (FloatObject(page_width), FloatObject(page_height))

    icc = DecodedStreamObject()
    icc.set_data(profile)
    icc.update({NameObject("/N"): NumberObject(3), NameObject("/Alternate"): NameObject("/DeviceRGB")})
    color_space = ArrayObject([NameObject("/ICCBased"), pdf._add_object(icc.flate_encode())])
    image = add_image(rgba.convert("RGB"), color_space)
    alpha = rgba.getchannel("A")
    if alpha.getextrema() != (255, 255):
        image[NameObject("/SMask")] = pdf._add_object(add_image(alpha, NameObject("/DeviceGray")))

    page[NameObject("/Resources")] = DictionaryObject({
        NameObject("/XObject"): DictionaryObject({NameObject("/Figure"): pdf._add_object(image)}),
    })
    drawing = DecodedStreamObject()
    drawing.set_data(f"q\n{page_width:f} 0 0 {page_height:f} 0 0 cm\n/Figure Do\nQ\n".encode("ascii"))
    page[NameObject("/Contents")] = pdf._add_object(drawing)
    pdf.add_metadata({"/Title": "ORBIT-MS NMI Figure 1"})
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.write(output_path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_png", type=Path)
    parser.add_argument("output_pdf", type=Path)
    parser.add_argument("--width-mm", type=Decimal, default=Decimal("180"))
    args = parser.parse_args()
    if not args.width_mm.is_finite() or not args.width_mm > 0:
        parser.error("--width-mm must be a finite positive number")
    export_png(args.input_png, args.output_pdf, args.width_mm)


if __name__ == "__main__":
    main()
