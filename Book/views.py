from django.shortcuts import render

from Reader.forms import ReaderDetails

books = [{"Author": "Agatha Christie", "Name": "Murder on Nile", "Genre": "Detective"},
         {'Author': "Agatha Christie", "Name": "Murder of Roger Ecroid", "Genre": "Detective"},
         {"Author": "Mario Piuso", "Name": "Godfather", "Genre": "Classic"},
         {"Author": "Stephen King", "Name": "Dreamcatcher", "Genre": "Thriller"},
         {"Author": "Jo Nesbo", "Name": "Headhunter", "Genre": "Detective"}]


def book_list(request):
    if ReaderDetails:
        return render(request, 'book_list.html', {'data': books})
