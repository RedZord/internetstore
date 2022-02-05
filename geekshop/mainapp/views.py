import json

from django.shortcuts import render

# Create your views here.

MENU_LINKS = [
    {"url": "index", "name": "домой"},
    {"url": "products", "name": "продукты"},
    {"url": "contact", "name": "контакты"},
]


def index(request):
    return render(
        request,
        "mainapp/index.html",
        context={"title": "Главная", "menu_links": MENU_LINKS},
    )


def products(request):
    with open("./products.json", "rb") as file:
        products = json.load(file)

    return render(
        request,
        "mainapp/products.html",
        context={
            "title": "Продукты",
            "menu_links": MENU_LINKS,
            "products": products
        },
    )


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={"title": "Контакты", "menu_links": MENU_LINKS},
    )
