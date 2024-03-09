from PIL import Image, ImageDraw, ImageFont
import os
def text_to_image(text,font_size="24",font_color="black",font_family="Arial", background_color="#FFFFFF",image_path="output.png"):
    # Create a blank image with white background
    font_size=int(font_size)
    image = Image.new("RGB", (500, 200), background_color)
    draw = ImageDraw.Draw(image)
    if font_family == "Arial":
        font_path = "arial.ttf"
    elif font_family == "Times New Roman":
        font_path = "times.ttf"
    elif font_family == "FORTE":
        font_path = "FORTE.TTF"
    else:
        font_path = "arial.ttf"
    # Choose a font and font size
    font = ImageFont.truetype(font_path, font_size)  # You may need to adjust the font path

    # Calculate text size and position
    text_width, text_height = draw.textsize(text, font)
    text_x = (image.width - text_width) // 2
    text_y = (image.height - text_height) // 2

    # Draw text on the image
    draw.text((text_x, text_y), text, fill=font_color, font=font)
    
    image.save(image_path)

    # Save the image

    return  image_path