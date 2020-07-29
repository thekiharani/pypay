from rest_framework import viewsets, permissions

from geeky.models import Note
from geeky.serializers import NoteSerializer, NoteListSerializer


class NoteView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Note.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return NoteListSerializer
        return NoteSerializer
