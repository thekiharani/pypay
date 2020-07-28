from rest_framework import viewsets, permissions

from geeky.models import Note
from geeky.serializers import NoteSerializer


class NoteView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
