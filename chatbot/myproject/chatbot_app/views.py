from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer
# Create your views here.

def chat(request):

    chatbot = ChatBot(**settings.CHATTERBOT)
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.korean")

    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        
        response = chatbot.get_response(user_input)
        return render(request, 'chatbot_app/chat.html', {'user_input':user_input, "response": response})
    
    return render(request, 'chatbot_app/chat.html')