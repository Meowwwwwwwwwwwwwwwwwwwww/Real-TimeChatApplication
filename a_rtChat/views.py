from django.shortcuts import render ,get_object_or_404 ,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import ChatmessageCreateforms
# Create your views here.

 
@login_required
def chatApp(request):
    chat_group = get_object_or_404(ChatGroup ,group_name="public_chat" )
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateforms()

    if request.htmx and request.method =="POST" :
        form = ChatmessageCreateforms(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context ={
                'message': message,
                 'user': request.user    
            }
            return render( request, 'a_rtchat/partials/chat_message_p.html',context)
    return render(request,'a_rtchat/chat.html', {'chat_messages': chat_messages,'form': form})