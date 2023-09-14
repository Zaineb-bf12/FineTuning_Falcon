from django.http import JsonResponse
from django.views.generic import View
import datetime
from langchain import HuggingFaceHub
import warnings
from langchain import PromptTemplate
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
import pyttsx3
from django.views.generic.base import View
from django.http import HttpResponse
apikey_hungingface = "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"

warnings.filterwarnings("ignore", category=UserWarning)



repo_id = "tiiuae/falcon-7b-instruct"
llm = HuggingFaceHub(huggingfacehub_api_token=apikey_hungingface,
                     repo_id=repo_id,
                     model_kwargs={"temperature":0.6, "max_new_tokens":500})


template = """
Vous êtes un assistant en intelligence artificielle.
L'assistant donne des réponses utiles, détaillées et polies à la question de l'utilisateur
Question : {question}\n\nRéponse : """
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

class ChatView(View):
    def get(self, request):
        # Récupérer les paramètres de la requête
        input_text = request.GET.get("input_text", "")

        # Utiliser le modèle LLM pour obtenir la réponse
        response = llm_chain.run(input_text)
        now = datetime.datetime.now()
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S %Z")
        data = {"message": input_text,
            "response": response ,
            "datetime": formatted_now}

        # Retourner la réponse au format JSON
        return JsonResponse({"response": data})
    

