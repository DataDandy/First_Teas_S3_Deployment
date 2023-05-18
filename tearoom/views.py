from .models import MenuItem
from .models import Review
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import Q
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .review import ReviewForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def index(request):
    return render(request, 'index.html', {})


def menu(request):
    menu_items = MenuItem.objects.all
    return render(request, 'menu.html', {'menu_items': menu_items})


def menu_drinks(request):
    drink_list = MenuItem.objects.filter(menu_is_a_Drink=True)
    return render(request, 'menu_drinks.html', {'drink_list': drink_list})


def menu_snacks(request):
    snack_list = MenuItem.objects.filter(menu_is_a_Drink=False)
    return render(request, 'menu_snacks.html', {'snack_list': snack_list})


def cart(request):
    return render(request, 'cart.html', {})

@login_required
def review(request):
    review_form = ReviewForm(request.POST, request.FILES)
    if review_form.is_valid():
        review_form.save()
        return HttpResponseRedirect(reverse('review'))
    else:
        review_form = ReviewForm()
    return render(request, 'create.html', {'review_form': review_form})


class ReviewList(generic.ListView):
    queryset = Review.objects.filter(status=1).order_by('review_date')
    template_name = 'review.html'
