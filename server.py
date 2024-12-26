"""
This module contains the Flask application for emotion detection. 
It includes routes for analyzing text and rendering the index page.
"""

from flask import Flask, render_template, request
from emotion_detection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_view():
    """
    Processes the user's input text, runs emotion detection,
    and returns a string summarizing the emotion analysis.

    Args:
        None

    Returns:
        str: A string with the emotion analysis result, including the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    result_string = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return result_string

@app.route("/")
def index():
    """
    Renders the index.html template when the root URL is accessed.

    Args:
        None

    Returns:
        str: The rendered index.html page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
