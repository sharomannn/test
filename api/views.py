from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.viewsets import ModelViewSet
from api import models, serializers

# Описание параметра
name_param = openapi.Parameter(
    'name',  # Имя параметра
    openapi.IN_QUERY,  # Тип передачи - query-параметр
    description="Имя для персонализации",  # Описание параметра
    type=openapi.TYPE_STRING,  # Тип данных
    required=False  # Параметр необязательный
)

@swagger_auto_schema(method='get', manual_parameters=[name_param])
@api_view(['GET'])
def hello_personalized(request):
    name = request.query_params.get('name', 'World')  # Получаем параметр name, по умолчанию 'World'
    return Response({"message": f"Helsi,lo, {name}!"})

class Authors(ModelViewSet):
    queryset = models.Authors.objects.all()
    serializer_class = serializers.Authors