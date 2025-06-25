# 🎙️ AI Radio Show Voice Assistant

This project is a modular voice-controlled assistant written in Python that acts like a **Radio Show Host**. It listens to voice commands and responds with:

- Latest news
- Weather updates
- Your favorite music
- Friendly greetings
- Exits on command ("bye") or keyboard (Ctrl + C)

---

## 📦 Features

- 🎧 Voice Input  
  Listens to your commands using `speech_recognition`.

- 🗣️ Text-to-Speech  
  Responds in a natural voice using `pyttsx3`.

- 🌤️ Weather Report  
  Gives real-time weather updates using the OpenWeatherMap API.

- 🗞️ News Headlines  
  Reads the top news headlines using the NewsAPI.

- 🎵 Music Streaming  
  Plays songs from YouTube using `yt_dlp` and VLC media player.

- ⌨️ Easy Exit  
  Just say "bye" or press Ctrl + C to stop the assistant.

---

## 🛠️ Tech Stack

- Python 3.x  
- speech_recognition  
- pyttsx3  
- yt_dlp  
- python-vlc  
- requests  
- APIs:
  - [OpenWeatherMap](https://openweathermap.org/)
  - [NewsAPI](https://newsapi.org/)

---

## 🗂️ Project Structure

- `main.py` – Core logic and voice command loop  
- `news.py` – News fetching module  
- `weather.py` – Weather fetching module  
- `music.py` – Music streaming functionality  
- `commands.py` – Extra command routing logic (optional)

---

## 🚀 How to Run

1. Install all the required Python libraries:
  run command in project directory(folder): pip install -r requirements.txt

3. Get your free API keys from:
- https://newsapi.org/
- https://openweathermap.org/api

3. Replace the placeholder API keys in the code files:
- `main.py`
- `news.py`
- `weather.py`
- `commands.py` (if used)

4. Start the assistant:
  run command in project directory(folder): python main.py
---

## 🎤 Example Voice Commands

- "hello"  
- "tell me the latest news"  
- "weather in Delhi"  
- "play Shape of You"  
- "bye"

---

## 🔥 Why This Project?

This assistant is perfect for:

- Students learning APIs and modular Python  
- Building cool final year or hobby projects  
- Creating hands-free, radio-style entertainment  
- Learning how to work with voice, audio, and real-time data in Python

---

## 🙌 Team & Credits

Made with ❤️ by creative Python developers using Open APIs and free tools.

---

## 📄 License

This project is intended for educational purposes. If you plan to deploy it publicly, ensure compliance with the usage terms of NewsAPI, OpenWeather, and YouTube.
   

