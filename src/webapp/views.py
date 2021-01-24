from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User

from src.WebAppraisal.forms import NewUserForm
from src.webapp.models import Profile

APPRAISER_ROLE = 'APPRAISER'
CUSTOMER_ROLE = 'CUSTOMER'

# empty url - redirect user to login/welcome page
def redirect_to_login(request):
    return redirect('/welcome/')

# login page - default when first opening the webapp
def login_view(request):
    return render(request, 'loginpage.html')

# for new users to create an account
def create_account_view(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.role = form.cleaned_data.get('user_role')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.save()

            raw_password = form.cleaned_data.get('password1')
            usr = authenticate(username=user.username, password=raw_password)
            login(request, usr)
            return redirect('/home/')

    else:
        form = NewUserForm()
    return render(request, 'sign-up.html', {'form': form})

# home page for both appraisers and their customers
def dashboard_view(request):
    current_user = User.objects.get(pk=request.user.id)
    return render(request, 'coming-soon.html', {'user': current_user})

