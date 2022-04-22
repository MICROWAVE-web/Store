from django.contrib import admin

from .models import *


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug', 'get_parent_title', 'created')
    list_filter = ('title', 'created')

    def get_parent_title(self, obj):
        return obj.parent.title

    get_parent_title.admin_order_field = 'parent__title'  # Allows column order sorting
    get_parent_title.short_description = 'Parent Title'  # Renames column head


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug', 'get_parent_title', 'created')
    list_filter = ('title', 'created')

    def get_parent_title(self, obj):
        if not obj.parent:
            return 'None'
        return obj.parent.title

    get_parent_title.admin_order_field = 'parent__title'  # Allows column order sorting
    get_parent_title.short_description = 'Parent Title'  # Renames column head


admin.site.register(PropertyValue)
admin.site.register(PropertyType)
