from datetime import datetime

from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic.simple import direct_to_template
from yadba.models import Entry, Category


def blog_index(request):
    entries_list = Entry.objects.all()
    return direct_to_template(request, template='yadba/index.html', extra_context={'entries_list': entries_list})

def blog_entry(request, year, month, slug):
    entries_list = get_list_or_404(Entry, date_posted__year=year, date_posted__month=month, slug=slug)
    return direct_to_template(request, template='yadba/index.html', extra_context={'entries_list': entries_list})

def blog_category(request, category):
    entries_list = get_list_or_404(Entry, categories__name=category)
    return direct_to_template(request, template='yadba/index.html', extra_context={'entries_list': entries_list})
