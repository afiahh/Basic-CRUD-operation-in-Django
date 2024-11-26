# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def welcome(request):
    return render(request, 'welcome.html')

# View All Entries
def diary_list(request):
    entries = DiaryEntry.objects.all().order_by('-date')
    return render(request, 'diary_list.html', {'entries': entries})

# View to read a specific diary entry
def diary_read(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk)
    return render(request, 'diary_read.html', {'entry': entry})

# Add a New Entry
def diary_create(request):
    if request.method == "POST":
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary_list')
    else:
        form = DiaryEntryForm()
    return render(request, 'diary_form.html', {'form': form})

# Update an Entry
def diary_update(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk)
    if request.method == "POST":
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('diary_list')
    else:
        form = DiaryEntryForm(instance=entry)
    return render(request, 'diary_form.html', {'form': form})

# Delete an Entry
def diary_delete(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('diary_list')  # Redirect to the diary list page
    return redirect('diary_list')  # Fallback redirect

