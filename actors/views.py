from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import Actor
from actors.serializer import ActorSerializer
from app.permissions import GlobalDefaultPermission


class ActorCreateLitsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyVies(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    