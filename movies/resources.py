from import_export import resources
from .models import movie
from import_export import widgets

class MovieResource(resources.ModelResource):
    #delete = fields.Field(widget=widgets.BooleanWidget())

    #def for_delete(self, row, instance):
    #    return self.fields['delete'].clean(row)


    class Meta:
        model = movie # default all fields
        #field = ( 'title', 'director', 'actor', 'categoryId', 'imbdUrl', 'coverUrl', 'viewDate', 'timeId', 'priceId', 'description', 'trailer', 'owner') #custom fields
        widget = {
            'viewDate': {'format': '%d-%m-%Y'},
        }