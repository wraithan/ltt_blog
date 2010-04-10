from django.shortcuts import render_to_response

from yadba.models import Entry


def blog_index(request):
    entry = Entry.objects.all()[0]
    return render_to_response('yadba/index.html', {'entry': entry})
