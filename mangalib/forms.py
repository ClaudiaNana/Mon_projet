from django import forms
from .models import Author, Book

class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset = Author.objects.all(), label = "Autheur")

    class Meta:
        model = Book
        fields = ['title', 'author','quantity']
        labels = {'title': 'Titre', 'quantity': 'Quantité' }

