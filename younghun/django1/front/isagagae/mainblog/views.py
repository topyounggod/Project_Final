from django.shortcuts import render, redirect
# from .models import Test
from django.http import HttpResponse
from django.urls import reverse
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)

def index(request) :
    return render(request, 'index.html')

def service(request) :
   return render(request,'service.html')

def result(request) :
   return render(request,'result.html')


# def memotest(request) :
#     user_input_str = request.POST['inputContent']
#     # 사용자 인풋값이 new_memo라는 변수에 저장됨
#     new_memo = Memo(content = user_input_str)
#     new_memo.save()
#     return redirect(reverse('showblog'))
#     # return HttpResponse('memotest임! =>'+user_input_str)
#
# def doneMemo(request) :
#     done_memo_id = request.GET['memoNum']
#     print('완료한 memo의 id', done_memo_id)
#     memo = Memo.objects.get(id = done_memo_id)
#     memo.delete()
#     return redirect(reverse('showblog'))
#
# def savestar(request) :
#     user_input_star = request.POST['value']
#     new_star = Star(content = user_input_star)
#     new_star.save()
#     return redirect(reverse('showblog'))


