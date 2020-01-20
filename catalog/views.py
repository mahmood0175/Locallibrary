from django.shortcuts import render
from django.views import generic
from . import models
# Create your views here.

def index(request):
    num_book = models.Book.objects.all().count()
    num_instance = models.BookInstance.objects.all().count()
    num_instance_available = models.BookInstance.objects.filter(status__exact='a').count()
    num_author = models.Author.objects.all().count()
    


    return render(request, 'catalog/index.html', {'num_book': num_book, 'num_instance':num_instance,
                                         'num_instance_available':num_instance_available,
                                         'num_author':num_author, })


# def Book_list(models.Model):
class BookListView(generic.ListView):
    model = models.Book
    template_name = "catalog/Book_list.html"

class  BookDetailView(generic.DetailView):
    model = models.Book
    template_name = "catalog/book_detail.html"  