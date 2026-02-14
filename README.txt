
Streaming Flask LLM Demo

Run:

pip install -r requirements.txt
python app.py

Test:

curl -N -X POST http://127.0.0.1:5000/stream \
-H "Content-Type: application/json" \
-d '{"prompt":"test","stream":true}'
