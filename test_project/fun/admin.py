from django.contrib import admin

from .models import Playground, FancyPlayground


class CartWheelAdmin(admin.ModelAdmin):
    change_form_template = 'fun/admin/playground/change_form.html'


class FancyCartWheelAdmin(admin.ModelAdmin):
    change_form_template = 'fun/admin/fancyplayground/change_form.html'


admin.site.register(Playground, CartWheelAdmin)
admin.site.register(FancyPlayground, FancyCartWheelAdmin)
