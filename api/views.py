from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.audioExtractor import extract_audio_data

@api_view(['GET'])
def search_audio_url(request):
    query = request.GET.get('query')
    if not query:
        return Response({'error': 'No search query provided'}, status=400)

    audio_url = extract_audio_data(query)
    if audio_url:
        return Response(audio_url)
    else:
        return Response({'error': 'Unable to find audio URL'}, status=500)
