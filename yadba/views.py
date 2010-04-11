from django.shortcuts import render_to_response

from yadba.models import Entry


def blog_index(request):
    entries_list = Entry.objects.all()
    return render_to_response('yadba/index.html', {'entries_list': entries_list})

def blog_view_entry(request, year, month, slug):
    return render_to_response('base.html')
