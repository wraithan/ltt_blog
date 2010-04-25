from models import Category, PoweredBy

def sidebar(request):
    category_list = Category.objects.all()
    return {'category_list': category_list}

def powered_by(request):
    powered_by = PoweredBy.objects.all()
    return {'powered_by': powered_by}
