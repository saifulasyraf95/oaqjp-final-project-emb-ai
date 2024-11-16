from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    # Get the text from the request JSON
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    # Use the emotion_detector function to get emotions and dominant emotion
    result = emotion_detector(text_to_analyze)

    # Format the output as requested
    response = {
        "anger": result['emotions']['anger'],
        "disgust": result['emotions']['disgust'],
        "fear": result['emotions']['fear'],
        "joy": result['emotions']['joy'],
        "sadness": result['emotions']['sadness'],
        "dominant_emotion": result['dominant_emotion']
    }

    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)