from django import forms
from .models import Order, Size, Kind

# class OrderForm(forms.Form):
#     kind = forms.ForeignKey(Kind, on_delete=models.CASCADE)
#     size = forms.ForeignKey(Size, on_delete=models.CASCADE)
#     # pic = forms.ImageField(upload_to='static/img/order')s
#     phone = forms.CharField(label="phone", max_length=225)
#     email = forms.EmailField(label="email", max_length=225)
    
#     kind.widget.attrs.update({'class': 'form-control'})
#     size.widget.attrs.update({'class': 'form-control'})
#     pic.widget.attrs.update({'class': 'form-control'})
#     phone.widget.attrs.update({'class': 'form-control'})
#     email.widget.attrs.update({'class': 'form-control'})

class OrderForm(forms.ModelForm):
    

    class Meta:
        model = Order
        fields = ['kind', 'size', 'pic', 'phone', 'email']
        labels = {'kind':'نوع نقاشی', 'size':'سایز', 'pic':'آپلود عکس', 'phone':'شماره موبایل', 'email':'ایمیل'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kind'].widget.attrs.update({'class': 'form-control'})
        self.fields['size'].widget.attrs.update({'class': 'form-control'})
        self.fields['pic'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'placeholder': ' +989029389002 به صورت مثال '})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

        

       
