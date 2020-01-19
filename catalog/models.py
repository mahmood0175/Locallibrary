from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.CharField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=200, help_text='13 caracture <a href="http://www.google.com" >isbn</a>')
    genre = models.ManyToManyField(Genre, help_text='select a genre for this book')

    def __str__(self):
        return self.title

    def get_absulot_url(self):
        return reverse('book_detail', args=[str(self.id)])


class BookInstance(models.Model):
    id =models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique id for this particular')
    book =models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateTimeField()

    LOAN_STATUS={
        ('a', 'Available'),
        ('o', 'OnLoan'),
        ('m', 'Maintnance'),
        ('r', 'Reserved'),
    }

    status = models.CharField(max_length=1,default='m', choices=LOAN_STATUS, blank=True, null=True)

    class Meta:
        ordering=['due_back']
    
    def __str__(self):
        return "{} {}".format(self.id, self.book.title)

class Author(models.Model):
    first_name= models.CharField(max_length=200) 
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField()
    date_of_death = models.DateTimeField()

    def get_absulot_url(self):
        return reverse('author_detail', args=[str(self.id)])

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)