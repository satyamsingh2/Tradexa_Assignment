from .models import Post
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password'
        )
        write_only_fields = ('password')

        

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'