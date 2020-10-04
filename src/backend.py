import io
import json

import numpy as np
from pydub import AudioSegment
from pydub.playback import play
from scipy.io import wavfile

from asr import recognize # voice recognition API
from tts import pronounce # text-to-speech API
#from chatbot import SmallTalkAgent # Smalltalk API

from utils import write_result

from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/tts', methods=['GET', 'POST'])
def handle_tts():
    """
    input:{
        "text":"English text without normalization"
    }
    :return: wav file bytes
    """

    content = request.get_json()
    sr, wav = pronounce(content.get('text'))
    wav = np.multiply(wav, (2 ** 15)).astype(np.int16)
    pcm = io.BytesIO()
    wavfile.write(pcm, rate=sr, data=wav)
    return send_file(pcm,
                     as_attachment=True,
                     attachment_filename='output.wav',
                     mimetype='audio/wav')


@app.route('/stt', methods=['GET', 'POST'])
def handle_asr():
    """
    input: wav file bytes
    :return: transcribed speech
    """
    data = "sorry I failed to recognize" #recognize()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response
