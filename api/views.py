from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MyDataSerializer

@api_view(['GET'])
def get_data(request):
    data = {
        'key1': 'value1',
        'key2': 123
    }

    serializer = MyDataSerializer(data)

    return Response(serializer.data)
