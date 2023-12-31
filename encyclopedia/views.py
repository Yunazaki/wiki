from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from . import util

def index(request):
    query = request.GET.get('q', '')
    if query:
        return redirect('page', title=query)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "query": query
    })

def page(request, title):
    if not util.get_entry(title):
        return HttpResponseNotFound()
    
    return render(request, "encyclopedia/page.html", {
        "entry": util.get_entry(title)
    })