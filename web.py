from flask import Flask, request
import detector as detector

from datetime import datetime

app = Flask(__name__)

@app.route('/check', methods=["POST"])
def handle_request():
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  print(f" {timestamp} Handle request")
  prompt = request.form.get("prompt")
  if not prompt:
    return {"error" : "prompt parameter required" }, 400
  detection = detector.detect(prompt)
  return {"spam": bool(detection)}

#app.run(host = "0.0.0.0", port=8000)