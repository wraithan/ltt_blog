from models import Category

def sidebar(request):
    category_list = Category.objects.all()
    return {'category_list':category_list}
