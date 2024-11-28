from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

from django.contrib.auth.decorators import login_required


def register(request):
    """Регистрирует нового пользователя."""
    if request.method != 'POST':
        # Выводит пустую форму регистрации.
        form = CustomUserCreationForm()
    else:
        # Обработка заполненной формы регистрации.
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление в личный кабинет.
            login(request, new_user)
            return redirect('users:dashboard')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

@login_required
def dashboard(request):

    return render(request, 'users/dashboard.html')
