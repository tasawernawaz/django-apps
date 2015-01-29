from django.contrib.auth.decorators import login_required
# from tasks.forms import LoginForm
# from tasks.models import Tasks
# from tasks.forms import TaskForm
# from tasks.forms import SignupForm


def user_login(request):
    pass


@login_required()
def user_logout(request):
    pass


@login_required()
def my_tasks(request):
    pass


@login_required()
def delete(request):
    pass


@login_required()
def send_email(request):
    pass


def user_signup(request):
    pass