from rest_framework import serializers
from .models import User, Role, LogActivite

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # On expose les champs définis dans ton modèle User
        fields = ('id', 'username', 'email', 'role_systeme', 'organisme', 'telephone', 'statut')

class LogActiviteSerializer(serializers.ModelSerializer):
    user_nom = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = LogActivite
        fields = '__all__'