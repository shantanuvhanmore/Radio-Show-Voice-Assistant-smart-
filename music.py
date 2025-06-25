import yt_dlp
import vlc
import time

def stream_song(song_name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
        'extract_flat': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{song_name}", download=False)
        if not info['entries']:
            print("No results found.")
            return
        video = info['entries'][0]
        stream_url = video['url']
        print(f"🎵 Now streaming: {video['title']}")

        # Stream using VLC
        instance = vlc.Instance('--no-xlib')
        player = instance.media_player_new()
        media = instance.media_new(stream_url)
        player.set_media(media)
        player.play()

        # Let it play until manually stopped
        while True:
            state = player.get_state()
            if state in (vlc.State.Ended, vlc.State.Error):
                break
            time.sleep(1)

song_name=input('enter song name: ')
stream_song(song_name)
