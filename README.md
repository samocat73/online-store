# Проект интернет-магазина
### Это мой проект интернет магазина написанный с использованием фреймворков Django и Bootstrap
## Запуск
*Выполните команду в терминале:*
```commandline
python manage.py runserver
```
*Далее перейдите по ссылке сервера из консоли:*
```commandline
http://127.0.0.1:8000/
```
Вы попадете на главную страницу. Нажмите на "Каталог", что бы увидеть каталог.
В приложении написано два пути. Главная и каталог.
```commandline
urlpatterns = [
    path('', home_view, name='home_view'),
    path('contacts/', contacts_view, name='contacts_view')
    ]
```
Их контроллеры просто генерируют html.
```commandline
from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')


def contacts_view(request):
    return render(request, 'contacts.html')
```
