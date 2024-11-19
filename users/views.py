from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Регистрирует нового пользователя."""
    if request.method != 'POST':
        # Выводит пустую форму регистрации.
        form = UserCreationForm()
    else:
        # Обработка заполненной формы регистрации.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу.
            login(request, new_user)
            return render(request, 'krusty_proxy/index.html')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'users:register.html', context)
