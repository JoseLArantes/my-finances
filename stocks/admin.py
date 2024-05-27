from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.urls import reverse
from .models import Stock, StockPrice
from .utils import fetch_stock_prices
from django.contrib import messages

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'action_buttons')

    def action_buttons(self, obj):
        return format_html('<a href="{}">Import Prices</a>', reverse('admin:stock_import_prices', args=[obj.code]))

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-prices/<str:stock_code>/', self.admin_site.admin_view(self.import_prices), name='stock_import_prices'),
        ]
        return custom_urls + urls

    def import_prices(self, request, stock_code):
        success, message = fetch_stock_prices(stock_code)
        if success:
            messages.success(request, message)
        else:
            messages.error(request, message)
        return HttpResponseRedirect(reverse('admin:stocks_stock_changelist'))

@admin.register(StockPrice)
class StockPriceAdmin(admin.ModelAdmin):
    list_display = ('stock', 'date', 'price')

