from django.contrib import admin
from .models import houseListingModel
# Register your models here.
@admin.register(houseListingModel)
class houseListingAdmin(admin.ModelAdmin):
    list_display=('title','price','square_feet','address','image')
    #list_editable=('title','price','square_feet')
    #prepopulated_fields={'id':('title')}
    #list_per_page= 5
    
#admin.site.register(houseListingModel)
    