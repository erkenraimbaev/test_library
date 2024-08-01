from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from librarians.models import Librarian
from readers.models import Reader


class RegisterView(CreateView):

    def form_valid(self, form):
        if self.form_valid:
            new_user = form.save()
            new_user.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context


class ProfileView(DetailView):

    def get_object(self, queryset=None):
        return self.request.user


class RegisterReader(RegisterView):
    model = Reader
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class RegisterLibrarian(RegisterView):
    model = Librarian
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
