from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  # ✅ Add this line
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Optional: Allow users to toggle completion
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