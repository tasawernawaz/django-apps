from rest_framework import serializers

from tasks_api.models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Tasks
        fields = ('user', 'short_summary', 'long_summary', 'url', 'created', 'updated')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
