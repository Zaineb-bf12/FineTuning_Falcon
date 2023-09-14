from django.views.generic import View
from django.http import HttpResponse, JsonResponse
import os
import pyttsx3
import base64


class convert_to_speech(View):
    def get(self, request):
        input_text = request.GET.get("input_text", "")

        # Initialize the speech synthesis engine
        engine = pyttsx3.init()

        # Convert text to speech
        engine.save_to_file(input_text, "speech.mp3")
        engine.runAndWait()

        # Get the path of the audio file
        audio_path = os.path.join(os.getcwd(), "speech.mp3")

        # Return the position of the audio file as JSON
        with open(audio_path, 'rb') as file:
            audio_data = base64.b64encode(file.read()).decode()
            
        return JsonResponse({'audioData': audio_data})