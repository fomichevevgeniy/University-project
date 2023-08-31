import gspread as gspread
from django.http import HttpResponse
from django.shortcuts import render, redirect
from google.oauth2.gdch_credentials import ServiceAccountCredentials

from .forms import *
from .models import *


# Create your views here.


def index(request):
    news = News.objects.filter(status=True)
    news = news.order_by('-created_at')
    if request.method == "POST":
        form = MainForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('index')
    else:
        form = MainForm()
    context = {
        "title": "Turon - Asosiy saxifa...",
        "form": form,
        "news": news[:3]
    }
    return render(request, 'university/index.html', context)


def news(request):
    categories = NewsCategory.objects.all()
    news = News.objects.filter(status=True)
    context = {
        "title": "Yangiliklar",
        "categories": categories,
        "news": news
    }
    return render(request, 'university/news.html', context)


def category_page(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = NewsCategory.objects.get(pk=category_id)
    categories = NewsCategory.objects.all()
    context = {
        'title': f"Kategoriya: {category.category_title}",
        'news': news,
        'categories': categories
    }

    return render(request, 'university/news.html', context)


def study(request):
    faculties = Faculty.objects.all()
    slider_images = SliderPhoto.objects.all()
    if request.method == "POST":
        form = MainForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('index')
    else:
        form = MainForm()
    context = {
        "title": "O‘quv faoliyati",
        "form": form,
        "faculties": faculties,
        "slider_images": slider_images
    }
    return render(request, "university/o'quvfaolyat.html", context)


def forstudents(request):
    articles = Article.objects.all()
    if request.method == "POST":
        form = MainForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('index')
    else:
        form = MainForm()
    context = {
        "title": "Talabalarga",
        "form": form,
        "articles": articles
    }
    return render(request, "university/students.html", context)


def contact(request):
    if request.method == "POST":
        form = MainForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('index')
    else:
        form = MainForm()
    context = {
        "title": "Kontaktlar",
        "form": form
    }
    return render(request, "university/contact.html", context)


def submission(request):
    if request.method == "POST":
        form = MainForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('index')
    else:
        form = MainForm()
    context = {
        "title": "Hujjat topshirish tartibi",
        "form": form
    }
    return render(request, "university/submission.html", context)


def document(request):
    if request.method == "POST":
        form = DocumentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            doc = Document.objects.create(**form.cleaned_data)
            print(doc)
            # YOUR DATA HERE
            configs = {
              "type": "",
              "project_id": "",
              "private_key_id": "",
              "private_key": "",
              "client_email": "",
              "client_id": "",
              "auth_uri": "",
              "token_uri": "",
              "auth_provider_x509_cert_url": "",
              "client_x509_cert_url": "",
              "universe_domain": ""
            }
            gc = gspread.service_account_from_dict(configs)
            sh = gc.open_by_url('YOUR URL HERE')
            # Отправка данных в таблицу
            data = [str(doc.pk),
                    str(doc.first_name),
                    str(doc.last_name),
                    str(doc.middle_name),
                    str(doc.birth_date),
                    str(doc.gender),
                    str(doc.region),
                    str(doc.district),
                    str(doc.address),
                    str(doc.phone_number),
                    str(doc.extra_phone_number),
                    str(doc.passport_photo.url),
                    str(doc.passport_series),
                    str(doc.passport_numbers),
                    str(doc.diploma_photo.url),
                    str(doc.faculty),
                    str(doc.study_type),
                    str(doc.exam_lang),
                    str(doc.application_data)
                    ]
            work = sh.worksheet('Лист1')
            work.insert_row(data)

            return redirect('index')
    else:
        form = DocumentForm()
    context = {
        "title": "Hujjat topshirish",
        "form": form
    }

    return render(request, "university/document.html", context)


def for_enroll(request):
    faculties = Faculty.objects.all()
    slider_images = SliderPhoto.objects.all()
    if request.method == "POST":
        form = MainForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('index')
    else:
        form = MainForm()
    context = {
        "title": "Abiturientlarga",
        "form": form,
        "faculties": faculties,
        "slider_images": slider_images
    }

    return render(request, "university/qabul.html", context)


def faculty_detail(request, faculty_id):  # TODO: ID
    faculty = Faculty.objects.get(pk=faculty_id)
    if request.method == "POST":
        form = MainForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('index')
    else:
        form = MainForm()

    context = {
        "title": "Ta'lim dasturi",
        "form": form,
        "faculty": faculty
    }

    return render(request, "university/international.html", context)


def news_detail(request, news_id):
    news = News.objects.get(pk=news_id)
    year, month, day = str(news.created_at).split()[0].split('-')

    data = dict(zip(news.image.all(), news.description.all()))

    context = {
        'news': news,
        'news_date': f"{day}/{month}/{year}",
        'data': data
    }

    return render(request, "university/news_detail.html", context)


def search_results(request):
    pass
