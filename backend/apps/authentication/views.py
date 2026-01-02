from rest_framework import viewsets
from .models import LogActivite, User, Role
from .serializers import LogActiviteSerializer, UserSerializer, RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LogActiviteViewSet(viewsets.ReadOnlyModelViewSet): # ReadOnly car on ne modifie jamais un log
    queryset = LogActivite.objects.all().order_by('-timestamp')
    serializer_class = LogActiviteSerializer