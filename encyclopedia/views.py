from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django import forms

from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput, label="Title")
    content = forms.CharField(widget=forms.Textarea, label="Content")

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
        "entry": util.get_entry(title),
        "title": title
    })

def newpage(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            if util.get_entry(title):
                warning_message = "Warning: Entry with this title already exists"
                return render(request, "encyclopedia/newpage.html", {
                    "form": NewPageForm(),
                    "warning_message": warning_message
                })
            
            util.save_entry(title, content)

            return redirect('page', title=title)

    return render(request, "encyclopedia/newpage.html", {
        "form": NewPageForm()
    })

def edit(request, title):
    return render(request, "encyclopedia/edit.html", {
        "title": title
    })