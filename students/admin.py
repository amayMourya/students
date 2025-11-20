from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'first_name', 'last_name', 'email', 'department', 'year_of_study', 'enrollment_date']
    list_filter = ['department', 'year_of_study', 'gender', 'enrollment_date']
    search_fields = ['student_id', 'first_name', 'last_name', 'email']
    readonly_fields = ['enrollment_date']
    
    fieldsets = (
        ('User Account', {
            'fields': ('user',)
        }),
        ('Personal Information', {
            'fields': ('student_id', 'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'gender', 'profile_picture')
        }),
        ('Address', {
            'fields': ('address', 'city', 'state', 'postal_code')
        }),
        ('Academic Information', {
            'fields': ('department', 'year_of_study', 'gpa', 'enrollment_date')
        }),
        ('Emergency Contact', {
            'fields': ('emergency_contact_name', 'emergency_contact_phone')
        }),
    )