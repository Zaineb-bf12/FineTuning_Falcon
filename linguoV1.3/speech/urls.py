from django.urls import path
from speech.views import convert_to_speech

urlpatterns = [
    path('convert/', convert_to_speech.as_view(), name='convert-to-speech'),
]