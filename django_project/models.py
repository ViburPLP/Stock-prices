from django.db import models

class StockPrice(models.Model):
    date = models.DateField()
    stock_symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.stock_symbol} - {self.date}: {self.price}"
