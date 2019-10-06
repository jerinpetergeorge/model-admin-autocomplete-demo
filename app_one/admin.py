from django.contrib import admin
from .models import Article
from model_admin_autocomplete import ModelAdminAutoComplete


# Register your models here.
class ArticleModelAdmin(ModelAdminAutoComplete, admin.ModelAdmin):
    autocomplete_fields = ('publications', 'reporter')


admin.site.register(Article, ArticleModelAdmin)
