from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic
from .forms import TopicForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    topics = Topic.objects.all()
    return render(request, 'crud_operations/home.html', {'topics': topics})

@login_required
def create(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TopicForm()
    return render(request, 'crud_operations/create.html', {'form': form})

@login_required
def read(request, id):
    topic = get_object_or_404(Topic, id=id)
    return render(request, 'crud_operations/read.html', {'topic': topic})

@login_required
def update(request, id):
    topic = get_object_or_404(Topic, id=id)
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TopicForm(instance=topic)
    return render(request, 'crud_operations/update.html', {'form': form})

@login_required
def delete(request, id):
    topic = get_object_or_404(Topic, id=id)
    topic.delete()
    return redirect('home')
