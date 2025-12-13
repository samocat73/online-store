from users.models import User
from django.views.generic import CreateView
from users.forms import UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.core.mail import send_mail
from config.settings import DEFAULT_FROM_EMAIL


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("catalog:home_view")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    @staticmethod
    def send_welcome_email(email):
        send_mail(
            subject='Добро пожаловать в магазин "ТехникаДома"',
            message="Спасибо за доверие к нашему магазину!",
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )
