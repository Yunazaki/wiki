from django.http import HttpResponseNotFound
from django.shortcuts import render

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    if not util.get_entry(title):
        return HttpResponseNotFound()
    
    return render(request, "encyclopedia/page.html", {
        "entry": util.get_entry(title)
    })