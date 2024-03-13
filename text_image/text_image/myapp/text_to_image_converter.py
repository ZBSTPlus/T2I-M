from PIL import Image, ImageDraw, ImageFont
import os
from io import BytesIO
import base64
from pathlib import Path
def text_to_image(text,font_size="24",font_color="black",font_family="Arial", background_color="#FFFFFF",image_path="output.png"):
    font_size=int(font_size)
    image = Image.new("RGB", (500, 200), background_color)
    draw = ImageDraw.Draw(image)
    font_path=""
    if font_family == "Arial":
        font_path = "arial.ttf"
    elif font_family == "Times New Roman":
        font_path = "times.ttf"
    elif font_family == "FORTE":
        font_path = "FORTE.TTF"
    else:
        font_path = "arial.ttf"
    font_path = Path.joinpath(Path(__file__).parent,font_path)
    font = ImageFont.truetype(font_path, font_size)  
    # text_width, text_height = draw.textsize(text, font)
    # text_x = (image.width - text_width) // 2
    # text_y = (image.height - text_height) // 2

    draw.text((100, 100), text, fill=font_color, font=font)
    
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    image.save(image_path)
    return  img_str.decode("utf-8")