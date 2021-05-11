from django.db import models

# Create your models here.
class Quote(models.Model):
    from_currency = models.CharField(max_length=5)
    to_currency = models.CharField(max_length=5)
    exchange = models.FloatField() # Better to replace with DecimalField if any computation is involved
    last_refreshed = models.DateTimeField()
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote-{self.id}-{self.last_refreshed.strftime('%d/%m/%y-%H:%M:%S')}"