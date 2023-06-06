from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import DailyTasksForm
from .models import DailyTask
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    # Render the home.html template
    return render(request, 'dailytasksapp/home.html')


def login_user(request):
    if request.method == 'GET':
        # If the request method is GET, render the loginuser.html template with an empty AuthenticationForm
        return render(request, 'dailytasksapp/loginuser.html', {'form': AuthenticationForm()})
    else:
        # If the request method is POST, authenticate the user and handle login
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            # If authentication fails, render the loginuser.html template with an AuthenticationForm and an error
            # message
            return render(request, 'dailytasksapp/loginuser.html', {'form': AuthenticationForm(),
                                                                    'error': 'Username and Password did not match'})
        else:
            # If authentication is successful, log in the user and redirect to 'currentdailytasks' view
            login(request, user)
            return redirect('currentdailytasks')


@login_required
def logout_user(request):
    if request.method == 'POST':
        # If the request method is POST, log out the user and redirect to the 'home' view
        logout(request)
        return redirect('home')


def signup_new_user(request):
    if request.method == 'GET':
        # If the request method is GET, render the signupnewuser.html template with an empty UserCreationForm
        return render(request, 'dailytasksapp/signupnewuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # If the passwords match, create a new user with the provided username and password
                user = User.objects.create_user(request.POST['username'], request.POST['password1'])
                user.save()
                # Log in the newly created user and redirect to 'currentdailytasks' view
                login(request, user)
                return redirect('currentdailytasks')

            except IntegrityError:
                # If the username already exists, render the signupnewuser.html template with a UserCreationForm and
                # an error message
                return render(request, 'dailytasksapp/signupnewuser.html', {'form': UserCreationForm(),
                                                                            'IntegrityError': 'username already exists. Enter a new username'})

        else:
            # If the passwords don't match, render the signupnewuser.html template with a UserCreationForm and an
            # error message
            return render(request, 'dailytasksapp/signupnewuser.html', {'form': UserCreationForm(),
                                                                        'error': 'passwords do not match. enter matching passwords'})


@login_required
def current_task(request):
    # Get all the current tasks for the logged-in user and render the currentdailytasks.html template
    dailyTasks = DailyTask.objects.filter(user=request.user, date_completed__isnull=True)
    return render(request, 'dailytasksapp/currentdailytasks.html', {'dailyTasks': dailyTasks})


@login_required
def completed_tasks(request):
    # Get all the completed tasks for the logged-in user, order them by date_completed, and render the
    # completedtasks.html template
    dailyTasks = DailyTask.objects.filter(user=request.user, date_completed__isnull=False

).order_by('-date_completed')
    return render(request, 'dailytasksapp/completedtasks.html', {'dailyTasks': dailyTasks})


@login_required
def view_task(request, task_pk):
    # Get the specific dailytask object for the logged-in user with the given task_pk
    dailytask = get_object_or_404(DailyTask, pk=task_pk, user=request.user)
    if request.method == 'GET':
        # If the request method is GET, render the viewtask.html template with the dailytask object and a form to
        # view/edit the task
        form = DailyTasksForm(instance=dailytask)
        return render(request, 'dailytasksapp/viewtask.html', {'dailytask': dailytask, 'form': form})
    else:
        try:
            # If the request method is POST, update the dailytask object with the form data and save it
            form = DailyTasksForm(request.POST, instance=dailytask)
            form.save()
            return redirect('currentdailytasks')
        except ValueError:
            # If there is a ValueError, render the viewtask.html template with the dailytask object, form,
            # and an error message
            return render(request, 'dailytasksapp/viewtask.html',
                          {'dailytask': dailytask, 'form': form, 'error': 'bad info'})


@login_required
def logout_user(request):
    if request.method == "POST":
        # If the request method is POST, log out the user and redirect to the 'home' view
        logout(request)
        return redirect('home')


@login_required
def create_task(request):
    if request.method == 'GET':
        # If the request method is GET, render the createtask.html template with an empty DailyTasksForm
        return render(request, 'dailytasksapp/createtask.html', {'form': DailyTasksForm()})
    else:
        try:
            # If the request method is POST, create a new DailyTask object with the form data and save it
            form = DailyTasksForm(request.POST)
            newDailyTask = form.save(commit=False)
            newDailyTask.user = request.user
            newDailyTask.save()
            return redirect('currentdailytasks')
        except ValueError:
            # If there is a ValueError, render the createtask.html template with an empty DailyTasksForm and an error
            # message
            return render(request, 'dailytasksapp/createtask.html',
                          {'form': DailyTasksForm(), 'Error': 'Bad information passed in. Try Again'})


@login_required
def complete_task(request, task_pk):
    # Get the specific dailytask object for the logged-in user with the given task_pk
    dailytask = get_object_or_404(DailyTask, pk=task_pk, user=request.user)
    if request.method == 'POST':
        # If the request method is POST, mark the dailytask as completed by setting the date_completed to the current
        # time and save it
        dailytask.date_completed = timezone.now()
        dailytask.save()
        return redirect('currentdailytasks')


@login_required
def delete_task(request, task_pk):
    # Get the specific dailytask object for the logged-in user with the given task_pk
    dailytask = get_object_or_404(DailyTask, pk=task_pk, user=request.user)
    if request.method == 'POST':
        # If the request method is POST, delete the dailytask object and redirect to the 'currentdailytasks' view
        dailytask.delete()
        return redirect('currentdailytasks')