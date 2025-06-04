

@app.route('/analyze_face', methods=['POST'])
def analyze_face():
    file = request.files['face_file']  # <-- use 'face_file' to match your HTML
    result = face_analysis.analyze(file)
    return result

if __name__ == '__main__':
    app.run(debug=True)