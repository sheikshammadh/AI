from flask import Flask, render_template, request
from modules import image_analysis, voice_analysis, wearable_analysis, face_analysis

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    file = request.files['image']
    result = image_analysis.analyze(file)
    return result

@app.route('/analyze_voice', methods=['POST'])
def analyze_voice():
    file = request.files['audio']
    result = voice_analysis.analyze(file)
    return result

@app.route('/analyze_wearable', methods=['POST'])
def analyze_wearable():
    file = request.files['data']
    result = wearable_analysis.analyze(file)
    return result

@app.route('/analyze_face', methods=['POST'])
def analyze_face():
    file = request.files['face_file']  # <-- use 'face_file' to match your HTML
    result = face_analysis.analyze(file)
    return result

if __name__ == '__main__':
    app.run(debug=True)