from comman.models import About
from blog.models import Post


def about_view(request):
    about = About.objects.first()

    context = {
        "about": about
    }
    return context

