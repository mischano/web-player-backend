from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.audioExtractor import search_and_extract_audio_url

@api_view(['GET'])
def search_audio_url(request):
    query = request.GET.get('query')
    if not query:
        return Response({'error': 'No search query provided'}, status=400)

    audio_url = search_and_extract_audio_url(query)
    if audio_url:
        return Response({'audio_url': audio_url})
    else:
        return Response({'error': 'Unable to find audio URL'}, status=500)
