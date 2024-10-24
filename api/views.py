from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.audioExtractor import extract_audio_data

@api_view(['GET'])
def search_audio_url(request):
    query = request.GET.get('query')
    if not query:
        return Response({'error': True, 'message': 'Query parameter is missing'}, status=400)

    audio_url = extract_audio_data(query)
    
    if audio_url:
        return Response(audio_url, status=200)
    else:
        return Response({'error': True, 'message': 'Audio data not found.'}, status=404)

