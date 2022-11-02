from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from users.producer import publish


class RegisterView(View):

    template_name='registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request=request, user=user)
            publish()
            return redirect('home')
        else:
            context = {
                'form': form
            }
        return render(request=request, template_name=self.template_name, context=context)