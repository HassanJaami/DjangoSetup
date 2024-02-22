from django import forms


class BookForm(forms.Form):
    Title = forms.CharField(label="Title", max_length=100)
    book_type = forms.CharField(label="book_type", max_length=100)
    author = forms.CharField(label="author", max_length=100)
    pub_date = forms.CharField(label="pub_date", max_length=100)