
from django.shortcuts import render
from django.http import HttpResponse
from .text_to_image_converter import text_to_image
from pathlib import Path


def index(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        font_size = request.POST.get('font_size', 24)
        font_color = request.POST.get('font_color', '#000000')
        background_color = request.POST.get('background_color', '#FFFFFF')
        font_family = request.POST.get('font_family', 'Arial')

        # custom_image_path = Path('C:/Users/HP/Desktop/text_image/text_image/text_image/myapp/static/images/output.png')
        custom_image_path = Path.joinpath(Path(__file__).parent, "output.png")
        print(custom_image_path)
        image_path = text_to_image(
            input_text, font_size, font_color, font_family, background_color, custom_image_path)
        return render(request, 'myapp/index.html', {'image_path': image_path})
    return render(request, 'myapp/index.html')


def download_image(request):

    image_path = Path.joinpath(Path(__file__).parent, "output.png")
    if image_path.exists():
        with open(image_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename="output.png"'
            return response
    else:
        return HttpResponse("Image file not found.")


def main(request):
    return render(request, 'myapp/main.html')
