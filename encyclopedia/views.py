from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from . import util

def index(request):
    entries = util.list_entries()
    query = request.GET.get('q', '').lower()

    if query in (entry.lower() for entry in entries):
        return redirect('page', title=query)
    elif query:
        return redirect('results', query=query)

    return render(request, "encyclopedia/index.html", {
        "entries": entries,
        "query": query
    })

def results(request, query):
    return render(request, "encyclopedia/results.html", {
        "query": query,
        "results": util.check_string(query)
    })

def page(request, title):
    if not util.get_entry(title):
        return HttpResponseNotFound()
    
    return render(request, "encyclopedia/page.html", {
        "entry": util.get_entry(title)
    })

def newpage(request):
    return render(request, "encyclopedia/newpage.html")