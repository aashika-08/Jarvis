# Jarvis - Voice Assistant 🧠🎙️

Jarvis is a simple voice-controlled virtual assistant built with Python.
It can perform tasks like opening websites, playing music, fetching the latest news, telling the current time, and more.
It interacts with users via voice using speech recognition and text-to-speech technologies.

# ✨ Features

- 🎤 Wake word detection ("Jarvis")
- 🌐 Opens websites like Google, Facebook, YouTube, LinkedIn
- 🎶 Plays predefined songs or searches on YouTube
- 📰 Fetches top news headlines using NewsAPI
- 🕒 Tells the current time
- 🔁 Voice interaction loop
- ❌ Exit via voice command with confirmation

# 🛠️ Technologies Used
```
- Python
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [Requests](https://pypi.org/project/requests/)
- [Webbrowser](https://docs.python.org/3/library/webbrowser.html)
- NewsAPI (for news)
```

# 📁 Project Structure
```
JARVIS/
├── **pycache**/
├── .venv/                  # Virtual environment (optional)
├── .env                    # Contains your NewsAPI key
├── config.py               # Configuration file to load API key
├── main.py                 # Main file to run the assistant
├── musicLibrary.py         # Dictionary of songs and their URLs
└── tempCodeRunnerFile.py   # Temporary file (can be ignored)

```
# 🔐 .env File

Create a `.env` file in the root directory and add your [NewsAPI](https://newsapi.org/) key like this:

```
NEWS\_API\_KEY=your\_api\_key\_here
```

# 📚 How to Run

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/jarvis-voice-assistant.git
   cd jarvis-voice-assistant
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your News API key** in a `.env` file as described above.

4. **Run the assistant:**

   ```bash
   python main.py
---

# 🎵 Adding Songs

Edit `musicLibrary.py` and add songs in this format:

```python
music = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA"
}
```

# 📌 Future Improvements

* Add weather info using OpenWeatherMap API
* Email and calendar integration
* Add GUI interface
* Use NLP to understand more complex queries
* Wake word detection using hotword detection libraries

# 👩‍💻 Author

**Aashika Jain**
Built with ❤️ for learning and personal use.

# 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute.
