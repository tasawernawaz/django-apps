# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tasks_api.models import Tasks
from tasks_api.serializers import TaskSerializer
from tasks_api.permissions import IsOwner


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    @list_route(methods=["GET"], permissions=(IsAuthenticated,IsOwner,))
    def my_tasks(self, request):
        serializer = TaskSerializer(Tasks.objects.get(user_id=self.kwargs['user_id']), many=True)
        return Response(serializer.data)



