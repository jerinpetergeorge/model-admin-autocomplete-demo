from model_admin_autocomplete import ModelAdminAutoComplete
from django.contrib import admin
from .models import *


class ArticleModelAdmin(ModelAdminAutoComplete, admin.ModelAdmin):
    autocomplete_fields = ('publications', 'reporter')
    autocomplete_search_fields = ('publications__title', 'reporter__first_name', 'reporter__last_name', 'reporter__email')


admin.site.register(Article, ArticleModelAdmin)
