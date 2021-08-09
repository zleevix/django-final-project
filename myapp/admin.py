from django.contrib import admin
from .models import Python2104, Place, Restaurant, Reporter, Article, Publication, BaiBao
class ReporterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
# Register your models here.
admin.site.register(Python2104)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Reporter, ReporterAdmin)
admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(BaiBao)