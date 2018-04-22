from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic,Entry
from .forms import TopicForm,EntryForm

# home page for learning log
def index(request):
    return render(request,'learning_logs/index.html')

# show all topics
@login_required
def topics(request):
    topics=Topic.objects.filter(owner=request.user).order_by('date_added')
    context={'topics':topics}
    return render(request,'learning_logs/topics.html',context)

# show a single topic and all its entries
@login_required
def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)    # DB queries
    if topic.owner!=request.user:
        raise Http404
    entries=topic.entry_set.order_by('-date_added') # sort in reverse order
    context={'topic':topic,'entries':entries}   # dictionary
    return render(request,'learning_logs/topic.html',context)

# add a new topic
@login_required
def new_topic(request):
    if request.method!='POST':
        form=TopicForm()    # no data submitted, hence creating a blank form
    else:
        # processing data from submitted post data
        form=TopicForm(request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context={'form':form}
    return render(request,'learning_logs/new_topic.html',context)

# add a new entry for a particular topic
@login_required
def new_entry(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    if topic.owner!=request.user:
        raise Http404
    if request.method!='POST':
        form=EntryForm()    # no data submitted, hence creating a blank form
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    
    context={'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

# editing an existing entry
@login_required
def edit_entry(request,entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    if topic.owner!=request.user:
        raise Http404
    if request.method!='POST':
        form=EntryForm(instance=entry)  # initial request, hence pre-filling the form with current entry
    else:
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    
    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)
