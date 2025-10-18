from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Show only the tasks that belong to the logged-in user."""
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Automatically assign the user when a task is created."""
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        task.completed = True
        task.save()
        return Response({'status': 'Task marked as complete'})

    @action(detail=True, methods=['post'])
    def mark_incomplete(self, request, pk=None):
        task = self.get_object()
        task.completed = False
        task.save()
        return Response({'status': 'Task marked as incomplete'})