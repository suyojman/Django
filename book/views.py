from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

# Create your views here.


def book_list(request):
    book_list = Book.objects.all()
    paginator = Paginator(
        book_list, 5
    )  # Here 5 denotes that only 5 elements will be allowed to display in one page
    page = request.GET.get("page")
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, "book/book_list.html", {"page": page, "books": books})
    # return render(request, 'book/book_list.html', {'book_list': book_list})


def book_create(request):
    data = {}

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            data["form_is_valid"] = True

        else:
            data["form_is_valid"] = False

    else:
        form = BookForm()

    context = {"form": form}
    data["html_form"] = render_to_string(
        "book/includes/partial_book_create.html", context, request=request
    )
    return JsonResponse(data)


@csrf_exempt
def book_edit(request,):
    data = {}
    if request.method == "GET":
        book_id = request.GET.get("book_id")
        post = get_object_or_404(Book, pk=book_id)
        form = BookForm(instance=post)
        context = {"form": form, "id": book_id}
        data["html_form"] = render_to_string(
            "book/includes/partial_book_update.html", context, request=request
        )

        return JsonResponse(data)

    if request.method == "POST":
        book_id = request.POST.get("book_id")
        instance = get_object_or_404(Book, id=book_id)
        form = BookForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            data["form_is_valid"] = True

        else:
            data["form_is_valid"] = False
        context = {"form": form}
    data["html_form"] = render_to_string(
        "book/includes/partial_book_update.html", context, request=request
    )
    return JsonResponse(data)


@csrf_exempt
def book_delete(request):
    if request.method == "POST":
        a = request.POST.get("bookid")
        Book.objects.filter(id=a).delete()
        return redirect("/book")
