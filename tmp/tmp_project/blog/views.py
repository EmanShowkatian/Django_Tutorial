from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse("Hello, World! Hello, Django!")


def api(request):

    data = {
        "1": {
            "title": "Hello Json",
            "id": 10,
            "slug": "first article",
        },
        "2": {
            "title": "Hello Json",
            "id": 20,
            "slug": "second article",
        },
        "3": {
            "title": "Hello Json",
            "id": 30,
            "slug": "third article",
        },
        "4": {
            "title": "Hello Json",
            "id": 40,
            "slug": "forth article",
        },
    }
    return(JsonResponse(data))
