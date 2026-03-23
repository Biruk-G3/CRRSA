from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    user = request.user

    context = {
        'role': user.role
    }

    return render(request, 'dashboard/dashboard.html', context)
