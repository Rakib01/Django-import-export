from django.contrib import admin
from .resources import BookResource

# Register your models here.
from .models import *
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export import resources, widgets
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
admin.site.register(Author)


class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        fields = ('id', 'name', 'author_name', 'author_email', 'price')


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
