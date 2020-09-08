from rest_framework import generics, mixins
from ..models import Cryptoseller
from .serializers import CryptoSerializer
from .permissions import IsOwnerOrReadOnly



class Crypthome( mixins.CreateModelMixin ,generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CryptoSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def get_queryset(self):
        return Cryptoseller.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def patch(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)