import yt_dlp

def extract_audio_data(query):
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

    try:
        with yt_dlp.YoutubeDL(search_opts) as ydl:
            search_result = ydl.extract_info(f"ytsearch:{query}", download=False)
        
        if search_result.get('entries'):
            video_info = search_result['entries'][0]
            video_url = video_info.get('url')
            
            if video_url:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl_audio:
                    audio_info = ydl_audio.extract_info(video_url, download=False)

                if audio_info and 'url' in audio_info:
                    return extract_info(audio_info)

 
    except yt_dlp.DownloadError as e:
        print(f"Download error: {e}")
    except Exception as e:
        print(f"An error occured: {e}")

    return None

def extract_info(audio_data):
    keys_to_extract = ['url', 'title', 'duration', 'channel', 'uploader', 'description', 'view_count']
    return {key: audio_data.get(key) for key in keys_to_extract}

