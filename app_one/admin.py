from model_admin_autocomplete import ModelAdminAutoComplete
from django.contrib import admin
from .models import *


class ArticleModelAdmin(ModelAdminAutoComplete, admin.ModelAdmin):
    autocomplete_fields = ('publications', 'reporter')


admin.site.register(Article, ArticleModelAdmin)
