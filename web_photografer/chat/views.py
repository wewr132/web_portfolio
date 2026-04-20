from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import ChatMessage
from .forms import MessageForm


@login_required
def chat_room(request):
    messages = ChatMessage.objects.filter(is_deleted=False).order_by('created_at')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.user = request.user
            msg.save()
            return redirect('chat:room')
    else:
        form = MessageForm()

    return render(request, 'chat/room.html', {'chat_messages': messages, 'form': form})
