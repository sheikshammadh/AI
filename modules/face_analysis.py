from PIL import Image
import numpy as np

def analyze(file):
    # Placeholder: In real use, run facial landmark/symptom detection
    img = Image.open(file.stream)
    arr = np.array(img)
    return f"Face image received. Shape: {arr.shape}. (Replace with real facial analysis.)"