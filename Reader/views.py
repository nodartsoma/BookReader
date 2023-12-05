from django.shortcuts import render

from Reader.forms import ReaderDetails


def reader_list(request):
    return render(request, "reader_list.html", {'form': ReaderDetails})
