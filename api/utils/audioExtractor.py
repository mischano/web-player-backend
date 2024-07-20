import yt_dlp

def search_and_extract_audio_url(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,  # Ensure only a single video is returned
    }

    search_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
        'extract_flat': True,  # Only fetch metadata, not actual media
    }

    with yt_dlp.YoutubeDL(search_opts) as ydl:
        search_result = ydl.extract_info(f"ytsearch:{query}", download=False)
        
        if 'entries' in search_result and len(search_result['entries']) > 0:
            video_info = search_result['entries'][0]
            video_url = video_info.get('url')
            if video_url:
                # Get audio URL from the found video
                with yt_dlp.YoutubeDL(ydl_opts) as ydl_audio:
                    audio_info = ydl_audio.extract_info(video_url, download=False)
                    if 'url' in audio_info:
                        return audio_info['url']
                    
    return None

        