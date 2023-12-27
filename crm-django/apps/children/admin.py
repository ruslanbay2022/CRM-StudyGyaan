from django.contrib import admin
from apps.children.models import Child


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_filter = ['gender', 'archived',]
    list_display = 'pk', 'name', 'middlename', 'surname', 'archived',
    list_display_links = 'pk', 'name', 'middlename', 'surname',
    ordering = 'surname', 'pk',
    search_fields = 'name', 'bio', 'pk', 'middlename', 'surname',

    # def bio_short(self, obj: Author) -> str:
    #     if len(obj.bio) < 100:
    #         return obj.bio
    #     else:
    #         return obj.bio[:100] + '.....'
