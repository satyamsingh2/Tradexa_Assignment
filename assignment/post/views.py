from rest_framework.generics import ListCreateAPIView
from .models import Post
from .serializer import UserSerializer, PostSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView
from django.contrib.auth.models import User


# Create your views here.

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class PostDetailView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    serializer_class = PostSerializer
    lookup_url_kwarg = "post_id"
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self):
        post_id = self.kwargs.get("post_id")
        return Post.objects.get(id=post_id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
