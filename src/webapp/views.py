from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from src.WebAppraisal.forms import NewUserForm
from src.webapp.models import Profile

APPRAISER_ROLE = 'APPRAISER'
CUSTOMER_ROLE = 'CUSTOMER'

# empty url - redirect user to login/welcome page
def redirect_to_login(request):
    return redirect('/welcome/')

# login page - default when first opening the webapp
def login_view(request):
    # TODO: Remove once logout button is functioning
  #  logout(request)
   # if request.user.is_authenticated:
    #    return redirect('/home')

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            clean_usn = form.cleaned_data['username']
            clean_pswd = form.cleaned_data['password']
            user = authenticate(username=clean_usn, password=clean_pswd)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/home")
                else:
                    return render(request, 'loginpage.html', {'form': form })
        else:
            pass
    else:
        form = AuthenticationForm()
    return render(request, "loginpage.html", {"form": form })

def logout_view(request):
    logout(request)
    return redirect('welcome/')

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

