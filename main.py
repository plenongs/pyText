from flask import Flask, redirect, url_for, request, jsonify
import requests as reqs
from wit import Wit

app = Flask(__name__)

def witAi(api, audi_type, lang):
  client = Wit(api)
  respond = None
  with open("audio", "rb") as wav:
    respond = client.speech(wav, {'Content-Type': audi_type})
  return respond

def save_audio(url):
  audio_get = reqs.get(url)
  typ_audio = "audio/wav"
  if "mp3" in audio_get.headers['Content-Type']:
    typ_audio = "audio/mpeg"
  with open("audio", "wb") as f:
    f.write(audio_get.content)
  return typ_audio

def convert_text(url, key, lang=None):
  respond = None
  error = None
  try:
    audio = save_audio(url)
    audio_text = witAi(key, audio, lang)
    if (respond:=audio_text.get("text")) == "":
      raise Exception("Result audio_text is None")
  except Exception as e:
    print(e)
    error = e
  return error, respond

@app.route("/")
def home():
  return "oppaiLibs - skmcmy"
  
@app.route("/api")
def api_error():
  return "POST /API/ACCESS_TOKEN \ndata = {'url': 'url audio grecaprcha'}"

@app.route("/api/<access_token>", methods=["POST"])
def api_get(access_token):
  respond_page = None
  try:
    g_audio = request.form.get("url")
    if g_audio != None:
      err, result = convert_text(g_audio, access_token)
      if err != None:
        raise Exception(err)
      respond_page = {"status": "success", "text": result}
    else:
      raise Exception("/POST url value not found!")
  except Exception as e:
    respond_page = {"status": "fail", "error": str(e)}
  return jsonify(respond_page)
  
if __name__ == '__main__':
   app.run(debug=False)
   