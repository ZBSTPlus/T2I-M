from django.shortcuts import render

# Create your views here
from django.http import HttpResponse
from .text_to_image_converter import text_to_image  # Import your text-to-image converter function
import os
from django.conf import settings
def index(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text','')
        # Call your text-to-image converter function
        font_size = request.POST.get('font_size', 24)  # Default font size is 24
        font_color = request.POST.get('font_color', '#000000')
        background_color = request.POST.get('background_color', '#FFFFFF')
        font_family = request.POST.get('font_family', 'Arial')
        # custom_image_path="C:\\Users\\chavva pallavi\\OneDrive\\Desktop\\text_image\\text_image\\myapp\\static\\images\\output.png"
        # custom_image_path = 'text_image\text_image\myapp\static\images\output.png'
        custom_image_path = 'C:\\Users\\HP\\Desktop\\text_image\\text_image\\text_image\\myapp\\static\\images\\output.png'
        image_path = text_to_image(input_text, font_size, font_color,font_family,background_color, custom_image_path)
        return render(request, 'myapp/index.html', {'image_path': image_path})
       
    return render(request,'myapp/index.html')
def download_image(request):
    # Replace with the actual image path
    # image_path = "text_image\text_image\myapp\static\images\output.png"
    # image_path = 'C:\Users\HP\Desktop\text_image\text_image\text_image\myapp\static\images\output.png'
    image_path = 'C:\\Users\\HP\\Desktop\\text_image\\text_image\\text_image\\myapp\\static\\images\\output.png'
    if os.path.exists(image_path):
        with open(image_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename="output.png"'
            return response
    else:
        return HttpResponse("Image file not found.")
def main(request):
    return render(request,'myapp/main.html')