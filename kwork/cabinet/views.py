from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from main.models import Customer


@login_required
def index(request):
    if request.user.is_customer:
        freelancers = Customer.objects.filter(is_customer=False)

        context = {
            'freelancers': freelancers
        }

    else:
        customers = Customer.objects.filter(is_customer=True)
        context = {
            'customers': customers
        }

    return render(request, 'cabinet/index.html', context)
