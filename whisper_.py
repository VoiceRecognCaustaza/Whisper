from django.http import JsonResponse
from django.conf import settings

settings.configure()

import whisper

def test_whisper_model(audio_file_path, language='English'):
    try:
        # Load the Whisper model
        model = whisper.load_model('base')

        # Transcribe the audio file
        result = model.transcribe(audio_file_path, language=language)
        print(result["text"])
    
        # Convert to JSON and return as response
        json_response = JsonResponse({"text": result["text"]})

        # Print or log the content of the JSON response
        print("JSON Response Content:", json_response.content)

        return json_response
    except Exception as e:
        # Handle any exceptions
        return(JsonResponse({"error": str(e)}, status=500))



# Replace 'path/to/your/audio/file.mp3' with the actual path to your audio file
audio_file_path = r'C:\\Users\\ASUS\\Desktop\\Caustaza\\Date-Issued-21-04-20-_3_.mp3'

# Test the Whisper model with the provided audio file
test_result = test_whisper_model(audio_file_path)
print(test_result)