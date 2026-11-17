"""Make a common-scale preview of the existing and redesigned figures."""
import argparse
from pathlib import Path
import subprocess

from PIL import Image, ImageDraw, ImageFont

arg = argparse.ArgumentParser(description=__doc__)
arg.add_argument("old", type=Path)
arg.add_argument("new", type=Path)
arg.add_argument("out", type=Path)
args = arg.parse_args()
font_path = subprocess.run(
    ["fc-match", "-f", "%{file}", "Arial"], capture_output=True, text=True
).stdout.strip() if Path("/usr/bin/fc-match").exists() else ""
font_path = font_path or "/System/Library/Fonts/Supplemental/Arial.ttf"
title = ImageFont.truetype(font_path, 36)
w = 1400
pad = 38
heading = 65
canvas = Image.new("RGB",(w*2+pad*3, round(w*9/16)+heading+pad*2), "#F1F4F5")
draw = ImageDraw.Draw(canvas)
for i,(name,file) in enumerate([("Previous artwork",args.old),("Redesigned framework",args.new)]):
    x=pad+i*(w+pad)
    image=Image.open(file).convert("RGB")
    image.thumbnail((w,round(w*9/16)),Image.Resampling.LANCZOS)
    draw.text((x,pad),name,font=title,fill="#30373C")
    canvas.paste(image,(x,pad+heading))
canvas.save(args.out,optimize=True)
