from email.mime.text import MIMEText
import smtplib
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from tasks.forms import LoginForm
from tasks.models import Tasks
from tasks.forms import TaskForm
from tasks.forms import SignupForm


def user_login(request):
    error = ''
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("my_tasks"))
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            user = authenticate(username=user_data['username'], password=user_data['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("my_tasks"))
                else:
                    error = "Inactive user"
            else:
                error = "Invalid user name or password"
        else:
            error = "Invalid values on form"
    else:
        form = LoginForm()
    return render(request, 'tasks\login.html', {'form': form, 'error': error})


@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


@login_required()
def my_tasks(request):
    error = ''
    user_id = request.user.id
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            task_id = form.get('task_id')
            if not task_id:
                task = Tasks()
            else:
                task = get_object_or_404(Tasks, pk=task_id)
            task.user_id = user_id
            task.short_summary = form['short_summary']
            task.long_summary = form['long_summary']
            task.updated = datetime.now()
            task.url = form['url']
            try:
                task.save()
            except IntegrityError as e:
                error = e.args[1]
            form = TaskForm()
    else:
        form = TaskForm()
    tasks_list = Tasks.objects.filter(user_id=user_id)
    paginator = Paginator(tasks_list, 5)
    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    return render(request, 'tasks/my_tasks.html', {'form': form, 'tasks_list': tasks, 'error': error})


@login_required()
def delete(request):
    error = ''
    task_id = request.POST.get("task_id")
    try:
        task = get_object_or_404(Tasks, pk=task_id)
        task.delete()
    except Exception as e:
        error = e.args[1]
    form = TaskForm()
    return render(request, 'tasks/my_tasks.html', {'form': form, 'error': error})


@login_required()
def send_email(request):
    EMAIL_HOST_USER = ' todotasks001@gmail.com'
    EMAIL_HOST_PASSWORD = 'todotasks'
    task_id = request.POST.get("task_id")
    task_obj = get_object_or_404(Tasks, pk=task_id)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    msg = MIMEText('Description: %s \n Url: %s' % (task_obj.long_summary, task_obj.url))
    msg['Subject'] = task_obj.short_summary
    error = ''
    try:
        server.sendmail(EMAIL_HOST_USER, request.user.email, msg.as_string())
    except Exception as e:
        error = e.args[1]
    form = TaskForm()
    return render(request, 'tasks/my_tasks.html', {form: 'form', 'error': error})


def user_signup(request):
    error = ''
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            if user_data['password'] != user_data['confirm_password']:
                error = "Passwords does not match"
            else:
                try:
                    new_user = User.objects.create_user(user_data['username'], user_data['email'],
                                                        user_data['password'])
                    new_user.first_name = user_data['first_name']
                    new_user.last_name = user_data['last_name']
                    new_user.save()
                    return HttpResponseRedirect("/tasks/my_tasks/")
                except IntegrityError as e:
                    error = e.args[1]

        else:
            error = "Invalid values on form"
    else:
        form = SignupForm()
    return render(request, 'tasks\signup.html', {'form': form, 'error': error})