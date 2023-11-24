from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate



def logout_account(request):
    logout(request)
    return redirect("/accounts/login/")



class Login(CreateView):
  def get(self, request):

    return render(request, "login.html")

  def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")



        else:
            return render(request, "login.html", {'error': "Parol yoki Login xato!"})

class Register(CreateView):

    def get(self, request):

        return render(request, "signup.html")
    def post(self, request, *args, **kwargs):
        from django.contrib.auth.models import User
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return render(request,"signup.html", {'error': 'Kiritilgan parol bir xil emas!'})
        user = authenticate(username=username, password= password1)
        if user:
            return render(request, "signup.html", {'error': 'Bunday akkaunt mavjud!'})

        UserN = User.objects.create_user(username=username, password=password1, is_staff=False)
        UserN.save()

        return redirect("/accounts/login/")





