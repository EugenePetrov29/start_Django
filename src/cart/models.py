from django.db import models
from django.contrib.auth import get_user_model
from groups.models import Book

User = get_user_model()

# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    def __str__(self):
        return f"{self.pk}"

    def total_summ(self):
        all_books = self.goods.all()
        total = 0
        for book in all_books:
            total += book.total_price
        return total
    

class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name='Cart',
        related_name='goods',
        on_delete=models.CASCADE
        )
    book = models.ForeignKey(
        'groups.Book',
        verbose_name="Book in the cart",
        related_name='books',
        on_delete=models.PROTECT
        )
    quantity = models.IntegerField("Quantity", default=1)
    price = models.DecimalField(
        "Price",
        max_digits=5,
        decimal_places=2
        )
    def __str__(self):
        return f"BookInCart #{self.pk} {self.book} quantity {self.quantity}"

    @property
    def total_price(self):
        return self.book.price * self.quantity