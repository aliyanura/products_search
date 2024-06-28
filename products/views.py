from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import ProductSearchSerializer, ProductOutputSerializer
from .services import ProductSearchService


class ProductAPIView(ViewSet):

    def list(self, request, *args, **kwargs):
        serializer = ProductSearchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        images = ProductSearchService.searc_simmilar_products(serializer.validated_data.get('file'))
        serializer = ProductOutputSerializer(images, many=True)
        return Response(data={
            'message': 'similar products',
            'data': serializer.data,
            'status': 'OK'
        }, status=status.HTTP_200_OK)