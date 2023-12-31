from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from . import util

def index(request):
    entries = util.list_entries()
    query = request.GET.get('q', '')
    if query in entries:
        return redirect('page', title=query)
    
    return render(request, "encyclopedia/index.html", {
        "entries": entries,
        "query": query
    })

def results(request):
    return render(request, "ecyclopedia/results.html", {
        "query": None
    })

def page(request, title):
    if not util.get_entry(title):
        return HttpResponseNotFound()
    
    return render(request, "encyclopedia/page.html", {
        "entry": util.get_entry(title)
    })