from django.contrib import admin
from .models import Specialty, Doctor, Education


class SpecialtyAdmin(admin.ModelAdmin):
    model = Specialty
    list_display = ['name',]


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1


class DoctorAdmin(admin.ModelAdmin):
    model = Doctor
    list_display = ['name', 'specialty',]
    inlines = [EducationInline]


admin.site.register(Specialty)
admin.site.register(Doctor, DoctorAdmin)
