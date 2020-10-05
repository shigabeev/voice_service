import io
import json

import numpy as np
from scipy.io import wavfile
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS

from tts import pronounce # text-to-speech API
from utils import write_result
app = Flask(__name__)
CORS(app)

@app.route('/tts', methods=['GET', 'POST'])
def handle_tts():
    """
    input: {"text":"English text without normalization"}
    :return: wav file bytes
    """
    try:
        content = request.get_json()
        text = content.get('text')
        write_result(text) # save request data
        if type(text) != str:
            return "Check the text.", 400
        if len(text) > 1000:
            return "Input length is too long.", 400
        sr, wav = pronounce()
        wav = np.multiply(wav, (2 ** 15)).astype(np.int16)
        pcm = io.BytesIO()
        wavfile.write(pcm, rate=sr, data=wav)
        return send_file(pcm,
                         as_attachment=True,
                         attachment_filename='output.wav',
                         mimetype='audio/wav')
    except Exception as e:
        print(e.message, e.args)
        return "Unexpected error occured. Message us to get a stable version of a product.", 500

if __name__ == "__main__":
    app.run()