from django.contrib import admin

from .models import Playground

class CartWheelAdmin(admin.ModelAdmin):
    change_form_template = 'fun/admin/change_form.html'

admin.site.register(Playground, CartWheelAdmin)
