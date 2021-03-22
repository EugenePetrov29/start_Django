from django.shortcuts import render
from django.views.generic import UpdateView
from . models import Status, OrderNew
from cart import models as cart_models
from accs import models as accs_models
from groups import models as groups_models


# Create your views here.
class OrderUpdate(UpdateView):
    model = OrderNew
    template_name = "order/checkout-cart.html"
    fields = (
        'address',
        'phone',
        'coment'
    )
    success_url = '/'
    def get_object(self, *args, **kwargs):
        current_cart_pk = self.request.session.get('current_cart_pk') #Получаем PK корзины из запроса
        print(current_cart_pk)
        if not current_cart_pk: #
            current_cart_pk = self.request.session.get('current_cart_pk') #
            if current_cart_pk: #
                current_cart = mod.Cart.objects.filter(pk=current_cart_pk).first() #
                return current_cart or [] #
            return [] #
        else: #
            current_castomer = self.request.user #Получаем текущего юзера
            if current_castomer.is_anonymous: #Если текущий юзер анонимный, то
                current_castomer = None #
                current_cart = cart_models.Cart.objects.get(pk = int(current_cart_pk))# Получаем объект корзины
                print(current_cart)
                book_in_cart = cart_models.BookInCart.objects.filter(cart = current_cart).all()#Получаем содержимое корзины
                status = Status.objects.get(pk=1)
                current_order_pk = self.request.session.get('current_order_pk')
                current_order, order_created = OrderNew.objects.get_or_create(
                    pk = current_order_pk,
                    defaults = {
                        'cart': current_cart,
                        'address': None,
                        'phone': None,
                        'coment': None,
                        'status': status
                    }
                )
                if order_created:
                    self.request.session['current_order_pk'] = current_order.pk
                return current_order #

            else:
                current_cart = cart_models.Cart.objects.get(pk = int(current_cart_pk))# Получаем объект корзины
                book_in_cart = cart_models.BookInCart.objects.filter(cart = current_cart).all()#Получаем содержимое корзины
                current_profile = self.request.user.profile
                status = Status.objects.get(pk=1)
                current_order_pk = self.request.session.get('current_order_pk')
                print(current_order_pk)
                current_order, order_created = OrderNew.objects.get_or_create(
                    pk = current_order_pk,
                    defaults = {
                        'cart': current_cart,
                        'address': current_profile.address,
                        'phone': current_profile.phone,
                        'status': status
                    }
                )
                print(order_created)
                if order_created:
                    self.request.session['current_order_pk'] = current_order.pk
                print(current_order_pk)
            return current_order #
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_cart_pk = self.request.session.get('current_cart_pk')
        current_cart = cart_models.Cart.objects.get(pk = int(current_cart_pk))
        context["book_in_cart"] = cart_models.BookInCart.objects.filter(cart = current_cart).all()
        context["current_cart"] = current_cart
        return context

    def get_success_url(self, **kwargs):
        success_url = super().get_success_url(**kwargs)
        current_cart_pk = self.request.session['current_cart_pk']
        current_cart = cart_models.Cart.objects.get(pk = int(current_cart_pk))
        if current_cart_pk:
            self.request.session['current_cart_pk'] = None
            self.request.session['current_order_pk'] = None
            return success_url
        #else:
        #    return  success_url