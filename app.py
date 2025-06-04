from flask import Flask, render_template, request
from models import AnalysisResult, SessionLocal
import face_analysis  # your analysis modules
import image_analysis
import voice_analysis
import wearable_analysis

app = Flask(__name__)

@app.route('/analyze_face', methods=['POST'])
def analyze_face():
    file = request.files['face_file']
    result = face_analysis.analyze(file)
    db = SessionLocal()
    db_result = AnalysisResult(
        analysis_type='face',
        filename=file.filename,
        result=result
    )
    db.add(db_result)
    db.commit()
    db.close()
    return result

@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    file = request.files['image_file']
    result = image_analysis.analyze(file)
    db = SessionLocal()
    db_result = AnalysisResult(
        analysis_type='image',
        filename=file.filename,
        result=result
    )
    db.add(db_result)
    db.commit()
    db.close()
    return result

@app.route('/analyze_voice', methods=['POST'])
def analyze_voice():
    file = request.files['audio_file']
    result = voice_analysis.analyze(file)
    db = SessionLocal()
    db_result = AnalysisResult(
        analysis_type='voice',
        filename=file.filename,
        result=result
    )
    db.add(db_result)
    db.commit()
    db.close()
    return result

@app.route('/analyze_wearable', methods=['POST'])
def analyze_wearable():
    file = request.files['wearable_file']
    result = wearable_analysis.analyze(file)
    db = SessionLocal()
    db_result = AnalysisResult(
        analysis_type='wearable',
        filename=file.filename,
        result=result
    )
    db.add(db_result)
    db.commit()
    db.close()
    return result

if __name__ == '__main__':
    app.run(debug=True)