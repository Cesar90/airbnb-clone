from django.http import HttpResponse
from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms, models

class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        username = models.User.objects.get(email=email).username
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    # def post(self, request):
    #     form = forms.LoginForm(request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data.get("email")
    #         password = form.cleaned_data.get("password")
    #         username = models.User.objects.get(email=email).username
    #         user = authenticate(request, username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect(reverse("core:home"))
    #     return render(request,  "users/login.html", {
    #         "form":form
    #     })
    
class LoginView_old(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request,  "users/login.html", {
            "form":form
        })

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            username = models.User.objects.get(email=email).username
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request,  "users/login.html", {
            "form":form
        })
    
def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))

# def login_view(request):
#     if request.method == "GET":
#         pass
#     elif request.method == "POST"