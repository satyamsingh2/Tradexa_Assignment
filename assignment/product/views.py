from rest_framework.generics import ListCreateAPIView
from .models import Product
from .serializer import ProductSerializer
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView


class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostDetailView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    serializer_class = ProductSerializer
    lookup_url_kwarg = "product_id"

    def get_object(self):
        product_id = self.kwargs.get("product_id")
        return Product.objects.get(id=product_id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)