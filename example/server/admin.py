from django.contrib import admin
from .models import PolarisUser, PolarisStellarAccount, PolarisUserTransaction


class PolarisUserAdmin(admin.ModelAdmin):
    list_display = "id", "first_name", "last_name", "email", "confirmed"


class PolarisStellarAccountAdmin(admin.ModelAdmin):
    list_display = "user", "account"


class PolarisUserTransactionAdmin(admin.ModelAdmin):
    list_display = "transaction", "account"


admin.site.register(PolarisUser, PolarisUserAdmin)
admin.site.register(PolarisStellarAccount, PolarisStellarAccountAdmin)
admin.site.register(PolarisUserTransaction, PolarisUserTransactionAdmin)
