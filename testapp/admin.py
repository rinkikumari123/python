from django.contrib import admin

from testapp.models import Student,AdminRegistraion

class StudentAdmin(admin.ModelAdmin):
    list_display = ["id","name","marks","roll_num","created_date","city","updated_date",]

admin.site.register(Student,StudentAdmin)

class Registraion(admin.ModelAdmin):
    list_display=["id","name","phone_no","email_id","city","gender","password",]

admin.site.register(AdminRegistraion,Registraion)
