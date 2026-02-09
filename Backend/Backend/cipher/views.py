from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def caesar_cipher(text, shift, mode="encode"):
    result = ""
    for char in text:
        code = ord(char)  # code Unicode du caractère
        if mode == "encode":
            new_code = (code + shift) % 1114111  # plage Unicode max
        else:  # decode
            new_code = (code - shift) % 1114111
        result += chr(new_code)
    return result

def cipher_api(request):
    text = request.GET.get("text", "")
    try:
        shift = int(request.GET.get("shift", 3))
    except ValueError:
        return JsonResponse({"error": "Décalage invalide"}, status=400)

    mode = request.GET.get("mode", "encode")  # "encode" ou "decode"
    result = caesar_cipher(text, shift, mode)
    return JsonResponse({"result": result})
