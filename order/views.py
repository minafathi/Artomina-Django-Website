from django.shortcuts import render
from .forms import OrderForm
from .models import Price


def order(request):
    if request.method == 'POST':
        filled_form = OrderForm(request.POST, request.FILES)
        if filled_form.is_valid():
            filled_form.save()
            # note = 'Thanks for ordring! Your %s %s painting is ordred successfully!' %(filled_form.cleaned_data['size'], filled_form.cleaned_data['kind'])
            note = 'متشکرم! سفارش نقاشی شما با موفقیت ثبت شد.'
            filled_form = OrderForm()
        else:
            note = 'سفارش شما ثبت نشد. دوباره تلاش کنید.'
            
        return render(request, 'order/order.html', {'orderform':filled_form, 'note':note, 'nbar': 'order'})
    else:
        form = OrderForm()
        return render(request, 'order/order.html', {'orderform':form, 'nbar': 'order'})

def price(request):
    price = Price.objects.all()
    return render(request, 'order/order.html', {'price':price})


