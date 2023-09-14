from django.urls import path
from chatAI.views import ChatView

urlpatterns = [
    path('chatAI/', ChatView.as_view(), name='chatAI'),

]