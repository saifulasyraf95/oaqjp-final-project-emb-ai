import requests

def emotion_detector(text_to_analyze):
    # Define the API endpoint and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    # Prepare the payload with the text to be analyzed
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send a POST request to the API
    response = requests.post(url, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()
        
        # Extract the emotion scores
        emotions = response_data['emotionPredictions'][0]['emotion']
        
        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Return the emotions and the dominant emotion
        return {
            "emotions": emotions,
            "dominant_emotion": dominant_emotion
        }
    else:
        # Handle errors or unsuccessful requests
        return f"Error: {response.status_code} - {response.text}"

# Example usage
# if __name__ == "__main__":
#     result = emotion_detector("I love data science")
#     print(result)