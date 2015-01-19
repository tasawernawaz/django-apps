from email.mime.text import MIMEText
import smtplib
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from tasks.forms import LoginForm
from tasks.models import Tasks
from tasks.forms import TaskForm


def index(request):
    return HttpResponse("home page")


def user_login(request):
    error = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            user = authenticate(username=user['username'], password=user['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("my_tasks"))
                else:
                    error = "Inactive user"
            else:
                error = "Invalid user name or password"
    else:
        form = LoginForm()
    return render(request, 'tasks\login.html', {'form': form, 'error': error})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


@login_required(login_url="/tasks/login/")
def my_tasks(request):
    error =''
    user_id = request.user.id
    if not user_id:
        return render(request, "tasks/login.html")
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                form = form.cleaned_data
                task_id = form.get('task_id')
                if not task_id:
                    task = Tasks()
                else:
                    task = Tasks.objects.get(id=task_id)
                task.user_id = user_id
                task.short_summary = form['short_summary']
                task.long_summary = form['long_summary']
                task.updated = datetime.now()
                task.url = form['url']
                task.save()
            except Exception as e:
                error = e.message
            form = TaskForm()
    else:
        form = TaskForm()
    tasks_list = Tasks.objects.filter(user_id=user_id)
    return render(request, 'tasks/my_tasks.html', {'form': form, 'tasks_list': tasks_list, 'error': error})


@login_required(login_url="/tasks/login/")
def delete(request):
    task_id = request.POST.get("task_id")
    try:
        t = Tasks.objects.filter(id=task_id)
        t.delete()
    except Exception as e:
        print e.message
    form = TaskForm()
    return render(request, 'tasks/my_tasks.html', {form: 'form'})


@login_required(login_url="/tasks/login/")
def send_email(request):
    EMAIL_HOST_USER = ' todotasks001@gmail.com'
    EMAIL_HOST_PASSWORD = 'todotasks'
    task_id = request.POST.get("task_id")
    t = get_object_or_404(Tasks, pk=task_id)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    msg = MIMEText('Description: %s \n Url: %s' % (t.long_summary, t.url))
    msg['Subject'] = t.short_summary
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = request.user.email
    server.sendmail(EMAIL_HOST_USER, ["tasawer.nawaz@arbisoft.com"], msg.as_string())
    form = TaskForm()
    return render(request, 'tasks/my_tasks.html', {form: 'form'})

