from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .models import Author
from .forms import NoteForm


def notes_list(request):
    """
    View to display all the notes created
    """

    notes = Note.objects.all()

    context = {
        'notes': notes,
        'page_title': 'List of Notes',
    }

    return render(request, 'notes/notes_list.html', context)


def note_detail(request, pk):
    """
    View to display details of a specific post
    """

    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})


def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            # if request.user.is_authenticated:
            #   note.author = request.user
            note.save()
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('notes_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('notes_list')
