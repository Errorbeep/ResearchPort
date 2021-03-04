from django.contrib import admin
from .models import ResearchArticles, Projects


# Register your models here.
class ResearchArticlesAdmin(admin.ModelAdmin):
    list_display = ('Rtitle', 'Rauthor', 'Rpublish')
    list_filter = ('Rpublish', 'Rauthor')
    search_fields = ('Rtitle', "Rinstitution")
    raw_id_fields = ("Rauthor",)
    date_hierarchy = "Rpublish"
    ordering = ['Rpublish', 'Rauthor']


admin.site.register(ResearchArticles, ResearchArticlesAdmin)


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('proj_name', 'charge_man', 'money_in_all', 'accomplish')
    list_filter = ('proj_name', 'charge_man', 'proj_type')
    search_fields = ('proj_name', )


admin.site.register(Projects, ProjectsAdmin)
