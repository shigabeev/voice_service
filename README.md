# Backend
Installation
```
pip install -r requirements.txt
```

To run
```   
export FLASK_APP=src/backend.py
flask run --host=0.0.0.0
```

## Usage
Send POST to backend/tts:5000 with your text in json:
```
{"text":"Your text goes here"}
```
You can find code samples in ```web/plugin.html```
