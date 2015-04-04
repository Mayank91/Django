from django.contrib import admin
from models import Expence
# Register your models here.
class ExpenceAdmin(admin.ModelAdmin):
    search_fields = ['date']
    list_display = ('spend_on','date')

admin.site.register(Expence,ExpenceAdmin)
