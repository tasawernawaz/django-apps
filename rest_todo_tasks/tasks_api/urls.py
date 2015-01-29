from django.conf.urls import url, patterns, include
from rest_framework.routers import DefaultRouter

from tasks_api.views import TasksViewSet
from rest_todo_tasks import settings


router = DefaultRouter()
router.register(r"tasks_api", TasksViewSet)
router.register(r'my_tasks/(?P<user_id>\d+)', TasksViewSet)
urlpatterns = patterns("",
                       url(r"^", include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls',
                                                  namespace='rest_framework')),
)