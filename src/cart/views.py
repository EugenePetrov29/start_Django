from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, TemplateView, UpdateView, CreateView, DeleteView, RedirectView
from . import models as mod
from django.urls import reverse, reverse_lazy
from groups import models as ref_models
from . import utils
# Create your views here.
class CartDetail(DetailView):
    template_name = "cart/add_to_cart.html"
    model = mod.Cart
    def get_object(self, *args, **kwargs):
        book_id = self.request.GET.get('book')
        if not book_id:
            current_cart_pk = self.request.session.get('current_cart_pk')
            if current_cart_pk:
                current_cart = mod.Cart.objects.filter(pk=current_cart_pk).first()
                return current_cart or []
            return []
        else:
            current_cart_pk = self.request.session.get('current_cart_pk')
            current_castomer = self.request.user
            if current_castomer.is_anonymous:
                current_castomer = None
            current_cart, cart_created = mod.Cart.objects.get_or_create(
                pk = current_cart_pk,
                defaults = {'customer': current_castomer}
            )
            if cart_created:
                self.request.session['current_cart_pk'] = current_cart.pk
            book = ref_models.Book.objects.get(pk=book_id)
            book_in_cart, book_created = mod.BookInCart.objects.get_or_create(
                cart = current_cart,
                book = book,
                defaults={'quantity': 1, 'price': book.price}
            )
            if not book_created:
                book_in_cart.quantity += 1
                book_in_cart.save()
        return current_cart

class RecalculateCart(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        current_cart_pk, cart_items = utils.harvest_date(self)
        if not current_cart_pk:
            return reverse("cart:add-to-cart")
        action = utils.update(cart_items, current_cart_pk)
        if action == "checkout":
            url = f"/order/checkout_cart/?current_cart_pk={current_cart_pk}"
            print(current_cart_pk)
        else:
            url = reverse("cart:add-to-cart")
        return url

