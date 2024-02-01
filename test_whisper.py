from django.http import JsonResponse
from django.conf import settings

settings.configure()

import whisper
import os
# Specify the directory containing audio files
audio_directory = r"C:\\Users\\ASUS\\Desktop\\Caustaza\\Codes\\Base"

# List all audio files in the directory
audio_files = [f for f in os.listdir(audio_directory) if f.endswith(".wav")]

# Initialize variables for accuracy calculation
total_accuracy = 0.0
total_loss = 0.0
total_files = 0
accuracy_list=[]



def test_whisper_model(audio_file_path, language='English'):
    try:
        # Load the Whisper model
        model = whisper.load_model('base')

        # Transcribe the audio file
        result = model.transcribe(audio_file_path, language=language)
        print(result["text"])
    
        # You might want to return the result for further use
        return result["text"]

    except Exception as e:
        # Handle any exceptions
        print({"error": str(e)})


# Iterate through each audio file
for audio_file in audio_files:
    audio_path = os.path.join(audio_directory, audio_file)
    # Test the Whisper model with the provided audio file
    test_result = test_whisper_model(audio_path)
    detected_words = test_result.lower().split()
    # Read corresponding text file
    txt_file_path = os.path.join(audio_directory, audio_file.replace(".wav", ".txt"))
    with open(txt_file_path, "r") as txt_file:
        target_words = txt_file.read().lower().split()

    # Compare transcribed text with target text
    accuracy = 0.0
    # Calculate accuracy based on detected words
    correct_words = [word for word in detected_words if word in target_words]
    accuracy = (len(correct_words) / len(target_words)) * 100 if len(target_words) > 0 else 0.0
    print(f"Précision pour {audio_file}: {accuracy:.2f}%")
    print(detected_words)
    accuracy_list.append(accuracy)
        # Accumulate accuracy for averaging
    total_accuracy += accuracy
    total_files += 1

# Calculate average accuracy
average_accuracy = total_accuracy / total_files if total_files > 0 else 0.0
print(f"Précision moyenne pour tous les fichiers: {average_accuracy}%")
