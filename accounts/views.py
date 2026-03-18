from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from locations.models import Agency
from django.http import JsonResponse
from locations.models import Woreda




def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Assign the only agency
            user.agency = Agency.objects.first()
            
            # Role-specific validation
            role = form.cleaned_data['role']
            if role == 'SUBCITY_ADMIN':
                if not form.cleaned_data['sub_city']:
                    form.add_error('sub_city', 'SubCity is required for SubCity Admin')
                user.woreda = None
            elif role == 'WOREDA_ADMIN':
                if not form.cleaned_data['sub_city'] or not form.cleaned_data['woreda']:
                    form.add_error('woreda', 'Woreda is required for Woreda Admin')
            elif role == 'WOREDA_STAFF':
                if not form.cleaned_data['sub_city'] or not form.cleaned_data['woreda']:
                    form.add_error('woreda', 'Woreda is required for Staff')
            
            if form.errors:
                return render(request, 'accounts/register.html', {'form': form})

            user.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def woredas_by_subcity(request, subcity_id):
    woredas = Woreda.objects.filter(sub_city_id=subcity_id).values('id', 'name')
    return JsonResponse(list(woredas), safe=False)

def users_cards(request):
    return render(request, "accounts/users_cards.html")