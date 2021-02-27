from django.shortcuts import render
from django.http import HttpResponse
from . models import update
from . models import aboutus
from . models import Astroh
from . models import Portfolio
from . models import Review
from . models import Contacts
from . forms import updateForm
from . forms import ContactsForm

 # Create your views here.

def home(request):
    template = 'index.html'
    return render(request, template)

def about(request):
    About = aboutus.objects.all()
    context = {'About':About}
    template = 'about.html'

    return render(request, template, context)

def portfolio(request):
    Port = Portfolio.objects.all()
    context = {'Port':Port}
    template = 'portfolio.html'

    return render(request, template, context)

def services(request):
    
    form = updateForm()

    Services = update.objects.all()
    context = {'Services':Services, 'form':form}
    template = 'services.html'

    return render(request, template, context)


def footer(request):
    template = 'footer.html'

    return render(request, template)

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()

   
    Rev = Review.objects.all()
    context = {'Rev':Rev}
    template = 'review.html'

    return render(request, template, context)

def joinus(request):
    template = 'joinus.html'

    return render(request, template)

def contacts(request):
    if request.method== 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ContactsForm()

    Conta = Contacts.objects.all()
    context ={'Conta':Conta,'form':form}
    template = 'contacts.html'
    return render(request, template, context)