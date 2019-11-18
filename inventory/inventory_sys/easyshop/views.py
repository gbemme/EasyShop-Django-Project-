from django.shortcuts import render, get_object_or_404,redirect
from .models import Product
from django.conf import settings
from .forms import PaymentForm

# Create your views here.
def index(request):
    return render(request,'index.html')


def show_product(request):
    products = Product.objects.filter()
    return render(request,'index.html',{'products':products})

def buy_product(request,pk):
    product = get_object_or_404(Product,pk=pk)
    # product.produty_quantiy= product.produty_quantiy-1
    return render(request,'buy_product.html',{'product':product})


def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit =False)
            payment.save()
            return redirect('message')

    else:
        form = PaymentForm()
    return render(request,'payment.html',{'form':form})


def message(request):
    return render(request,'message.html')


