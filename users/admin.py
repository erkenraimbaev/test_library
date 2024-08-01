from django.contrib import admin

from readers.models import Reader


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone',)
    list_filter = ()
    search_fields = ('email',)
