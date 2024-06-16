from django.urls import path
from .views import notes_list, note_detail, note_create, note_update, note_delete


urlpatterns = [
    path('', notes_list, name='notes_list'),

    path('notes/<int:pk>/', note_detail, name='note_detail'),

    path('notes/new/', note_create, name='note_create'),

    path('notes/<int:pk>/edit/', note_update, name='note_update'),

    path('notes/<int:pk>/delete/', note_delete, name='note_delete'),
]
