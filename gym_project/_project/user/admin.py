from django.contrib import admin

from .models import Sale, Payment, Client, RecentAction


admin.site.register(Sale)
admin.site.register(Payment)
admin.site.register(Client)
admin.site.register(RecentAction)