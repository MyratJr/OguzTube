from django.contrib import admin
from .models import *


user={
    'dildar' : "dildar",
    'gulbahar' : "gulbahar",
    "myratjr" : "myratjr"
    }


class PropertyVideoInline(admin.StackedInline):
    model = Video


class PropertyShortsInline(admin.StackedInline):
    model = Shorts


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyVideoInline, PropertyShortsInline]
    fields = ('username', 'first_name', 'last_name', 'email', 'avatar')
    extra_fields = ('password', 'user_permissions', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
 
    def get_fields(self, request, instance):
        fields = super().get_fields(request, instance)

        if request.user.is_superuser:
            fields += self.extra_fields
        
        return fields

    def get_queryset(self, request):
        if not request.user.is_superuser:
            return super().get_queryset(request).filter(id=request.user.id)
        return super().get_queryset(request)    

    class Meta:
        model = User


admin.site.register(User, PropertyAdmin)