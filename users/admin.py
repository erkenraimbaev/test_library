from django.contrib import admin

from users.models import Reader, Librarian


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone',)
    list_filter = ()
    search_fields = ('email',)


@admin.register(Librarian)
class Admin(admin.ModelAdmin):
    list_display = ('username', 'personnel_number',)
    list_filter = ('is_active',)
    search_fields = ('email',)
