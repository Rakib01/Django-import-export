from import_export import resources
from .models import *
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget


class BookResource(resources.ModelResource):
    Author = fields.Field(
        column_name='author_name',
        attribute='Author',
        widget=ForeignKeyWidget(Author, 'author_name'))
    Author = fields.Field(
        column_name='author_email',
        attribute='Author',
        widget=ForeignKeyWidget(Author, 'author_email'))

    class Meta:
        model = Book
        fields = ('id', 'name', 'author_name', 'author_email', 'price')
        export_order = ('id', 'price', 'author', 'author_email', 'name')
