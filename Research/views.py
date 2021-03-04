from django.shortcuts import render, get_object_or_404
from .models import ResearchArticles, Projects


# Create your views here.

def Article(request):
    articles = ResearchArticles.objects.all()
    projects = Projects.objects.all()
    return render(request, "REArticle/article.html", {"articles": articles, "projects": projects})


def manage(request):
    return render(request, "admin/base_site.html")


def admin(request):
    return render(request, "admin/base_site.html")


def articleContent(request, id):
    arcGetCon = get_object_or_404(ResearchArticles, id=id)
    return render(request, "REArticle/content.html", {"article": arcGetCon})


def projectContent(request, id):
    arcGetCon = get_object_or_404(Projects, id=id)
    return render(request, "REArticle/projContent.html", {"project": arcGetCon})
