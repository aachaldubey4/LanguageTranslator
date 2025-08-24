from flask import Flask, render_template, request
from googletrans import Translator
from gtts import gTTS
import os

app = Flask(__name__)
translator = Translator()

# Make sure static folder exists
if not os.path.exists("static"):
    os.makedirs("static")

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        text = request.form["text"]
        src_lang = request.form["src_lang"]
        dest_lang = request.form["dest_lang"]

        # Translation
        result = translator.translate(text, src=src_lang, dest=dest_lang)
        translated_text = result.text

        # Save speech file in static/
        tts = gTTS(translated_text, lang=dest_lang)
        tts.save(os.path.join("static", "output.mp3"))

    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
