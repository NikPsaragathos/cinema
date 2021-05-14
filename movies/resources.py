from import_export import resources
from .models import movie

class MovieResource(resources.ModelResource):
    #delete = fields.Field(widget=widgets.BooleanWidget())

    #def for_delete(self, row, instance):
    #    return self.fields['delete'].clean(row)


    class Meta:
        model = movie # default all fields
        #field = ( 'title', 'director', 'actor', 'categoryId', 'imbdUrl', 'coverUrl', 'viewDate', 'timeId', 'priceId', 'description', 'trailer', 'owner') #custom fields
        #widgets = {
        #    'published': {'format': '%d.%m.%Y'},
        #}