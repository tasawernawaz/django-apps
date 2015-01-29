
from django.conf.urls import url, patterns
from tasks.views import user_login, my_tasks, delete, send_email, user_logout, user_signup
from django.views.generic import RedirectView
from rest_todo_tasks import settings

urlpatterns = patterns("",
                       url(r"^login/$", user_login, name="login"),
                       url(r"^logout/$", user_logout, name="logout"),
                       url(r"^signup/$", user_signup, name="signup"),
                       url(r"^my_tasks/$", my_tasks, name="my_tasks"),
                       url(r"^delete/$", delete, name="delete"),
                       url(r"^email/$", send_email, name="email"),


)

