import pyttsx3
import speech_recognition as sr
import re
import requests
import yt_dlp
import vlc
import time
import os

# --------------- CONFIG ----------------
# Replace with your actual API key as a string with "os.getenv("NEWS_API_KEY")"
# Replace with your actual API key as a string with "os.getenv("WEATHER_API_KEY")"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")           
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# --------------- TEXT TO SPEECH ----------------
engine = pyttsx3.init()
engine.setProperty("rate", 160)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# --------------- SPEECH TO TEXT ----------------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"You: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t get that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

# --------------- NEWS MODULE ----------------
def get_latest_news(num_articles=3, country='us'):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'ok':
            articles = data['articles'][:num_articles]
            for i, article in enumerate(articles, 1):
                speak(f"Headline {i}: {article['title']}")
        else:
            speak("Couldn't fetch news.")
    except Exception:
        speak("Error while getting news.")

# --------------- WEATHER MODULE ----------------
def get_weather(city):
    try:
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={WEATHER_API_KEY}"
        geo_data = requests.get(geo_url).json()
        if not geo_data:
            speak(f"Couldn't find location {city}.")
            return
        lat, lon = geo_data[0]['lat'], geo_data[0]['lon']
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
        weather_data = requests.get(weather_url).json()
        temp = weather_data['main']['temp']
        condition = weather_data['weather'][0]['description']
        speak(f"The current temperature in {city} is {temp}°C with {condition}.")
    except:
        speak("Couldn't retrieve weather data.")

# --------------- MUSIC MODULE ----------------
def play_song(song_name):
    try:
        speak(f"Playing {song_name} , to Stop music press ctrl + c")
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'noplaylist': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{song_name}", download=False)
            video = info['entries'][0]
            url = video['url']

        instance = vlc.Instance('--no-xlib')
        player = instance.media_player_new()
        media = instance.media_new(url)
        player.set_media(media)
        player.play()

        while True:
            state = player.get_state()
            if state in (vlc.State.Ended, vlc.State.Error):
                break
            time.sleep(1)

    except KeyboardInterrupt:
        speak("Song interrupted.")
        player.stop()
    except Exception:
        speak("Could not play the song.")

# --------------- MAIN LOOP ----------------
def run_radio_assistant():
    speak("Hey there everyone! I’m your AI Radio Show Host. welcoome to the show")
    speak("""
╔════════════════════════════════════════════════════════════════════╗
║                      Radio Show Voice Commands                     ║
╠════════════════════════════════════════════════════════════════════╣
║       To know about News:                                          ║
║     ➤ Say: 'today's headline'                                      ║
║            'latest news'                                           ║
║            'news updates'                                          ║
║                                                                    ║
║      To know about Weather:                                        ║
║     ➤ Say: 'weather in London'                                     ║
║            'weather in Mumbai'                                     ║
║                                                                    ║
║      To stream your favorite Music:                                ║
║     ➤ Say:'play Despacito'                                         ║
║            'play blue'                                             ║
║                                                                    ║
║      To stop music:                                                ║
║     ➤ Press: Ctrl + C                                              ║
╚════════════════════════════════════════════════════════════════════╝
""")

    while True:
        try:
            command = listen()
            if not command:
                continue

            # Greetings
            if re.search(r'\b(hi|hello|hey)\b', command):
                speak("Hello there! What would you like to hear today?")

            # News
            elif re.search(r'\b(news|headlines|latest|updates)\b', command):
                get_latest_news()

            # Weather
            elif "weather" in command:
                city_match = re.search(r'weather in ([\w\s]+)', command)
                if city_match:
                    city = city_match.group(1)
                    get_weather(city)
                else:
                    speak("Please say something like 'weather in Delhi'.")

            # Music
            elif "play" in command:
                song_match = re.search(r'play (.+)', command)
                if song_match:
                    song = song_match.group(1)
                    play_song(song)
                else:
                    speak("Tell me which song to play.")

            # Exit
            elif re.search(r'\b(exit|quit|bye)\b', command):
                speak("Signing off from your AI Radio Show. Take care!")
                break

            else:
                speak("Hmm, I didn’t get that. Try saying news, weather, or play followed by a song.")

        except KeyboardInterrupt:
            speak("Interrupted. Ready for your next command!")

# --------------- START ----------------
if __name__ == "__main__":
    run_radio_assistant()
