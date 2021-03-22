from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name="Статус", null=True, blank=True)

    def __str__(self):
        return f'ID: {self.pk} status: {self.name}'

# Create your models here.
class OrderNew(models.Model):
    cart = models.OneToOneField(
        "cart.Cart",
        verbose_name="Cart",
        related_name="cart",
        on_delete=models.PROTECT
        )
    address = models.CharField("Адрес доставки", max_length=200, blank=False, null=True)
    phone = models.IntegerField("Контактный номер телефона", default=375, blank=False, null=True)
    status = models.ForeignKey(Status, verbose_name="Статус заказа", on_delete=models.PROTECT, default=1, null=True, blank=True)
    coment = models.TextField("Комментарии", blank=True, null=True, default=None)
    
    def __str__(self):
        return f"order {self.pk}"
