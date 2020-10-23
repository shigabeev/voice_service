import io
import os
import json
import logging

import numpy as np
from scipy.io import wavfile
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS

from tts import pronounce # text-to-speech API
from utils import write_result


app = Flask(__name__)
CORS(app)
CACHEDIR = os.path.dirname(os.path.abspath(__file__)) + "/cache"
os.makedirs(CACHEDIR, exist_ok=True)


@app.route('/tts', methods=['GET', 'POST'])
def handle_tts():
    """
    input: {"text":"English text without normalization",
            "type": "wav|ogg" # TODO
            "batched": 0 # TODO
            "cached": 0 # TODO
            }
    :return: wav file bytes
    """
    try:
        content = request.get_json()
        text = content.get('text')
        audio_type = content.get('type', 'wav')

        text_proc = text.strip()
        fname = f"{hash(text_proc)}.{audio_type}"
        fpath = f"{CACHEDIR}/{fname}"

        write_result(text) # save request data
        if type(text) != str:
            return "Input is incorrect. Check if it's the text.", 400
        if len(text) > 1000:
            return "Input length is too long. Message us to get a full version of a product.", 400

        # Process sound
        if not fname in os.listdir(CACHEDIR):
            sr, wav = pronounce(text)
            wav = np.multiply(wav, (2 ** 15)).astype(np.int16)
            wavfile.write(fpath, rate=sr, data=wav)

        return send_file(fpath,
                 as_attachment=True,
                 attachment_filename='output.wav',
                 mimetype='audio/wav')
    except Exception as e:
        print(e)
        return "Unexpected error occured. Message us to get a stable version of a product.", 500

