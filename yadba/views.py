from datetime import datetime

from django.shortcuts import render_to_response, get_list_or_404
from yadba.models import Entry


def blog_index(request):
    entries_list = Entry.objects.all()
    return render_to_response('yadba/index.html', {'entries_list': entries_list})

def blog_view_entry(request, year, month, slug):
    entries_list = get_list_or_404(Entry, date_posted__year=year, date_posted__month=month, slug=slug)
    return render_to_response('yadba/index.html', {'entries_list': entries_list})
