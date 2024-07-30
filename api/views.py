from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.audioExtractor import extract_audio_data

@api_view(['GET'])
def search_audio_url(request):
    query = request.GET.get('query')
    if not query:
        return Response({'error': True})
        # return Response({'error': True}, status=400)

    audio_url = extract_audio_data(query)
    if audio_url:
        audio_url['error'] = False
        return Response(audio_url)
    else:
        return Response({'error': True})
        # return Response({'error': True}, status=500)
