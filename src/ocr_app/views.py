from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import base64
import pytesseract
from PIL import Image

# Create your views here.


def index(request):
    if request.method == "POST":
        try:
            image = request.FILES["imagefile"]
            # encode image to base64 string
            image_base64 = base64.b64encode(image.read()).decode("utf-8")
        except:
            messages.add_message(
                request, messages.ERROR, "No image selected or uploaded"
            )
            return render(request, "home.html")

        text = pytesseract.image_to_string(Image.open(image))
        print(f'text: {text}')
        if text:
            text = text.split('\n')
        else:
            text = ""
        # return text to html
        return render(request, "ocr_app/index.html", {"ocr_text": text, "org_imag": image_base64, "results": True})

    return render(request, "ocr_app/index.html", {"results": False})