from django.shortcuts import render


def main_page(request):
    title = 'Главная'
    return render(request, 'pages/main.page.html', {'title': title})


def about_page(request):
    title = 'О нас'
    return render(request, 'pages/about.page.html', {'title': title})


def price_page(request):
    title = 'Цены'
    return render(request, 'pages/price.page.html', {'title': title})


def contacts_page(request):
    title = 'Контакты'
    return render(request, 'pages/contacts.page.html', {'title': title})


def partners_page(request):
    title = 'Партнеры'
    return render(request, 'pages/partners.page.html', {'title': title})
