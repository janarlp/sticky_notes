from django.test import TestCase
from django.urls import reverse
from .models import Note, Author

test_title = 'Test New Note'
test_note_content = 'This is a test note'


class NoteModelTest(TestCase):
    def setUp(self) -> None:
        author = Author.objects.create(name='Test Author')
        Note.objects.create(
            title=test_title, content=test_note_content, author=author)

    def test_note_title(self):
        note_one = Note.objects.get(id=1)
        self.assertEqual(note_one.title, test_title)

    def test_note_content(self):
        note_one = Note.objects.get(id=1)
        self.assertEqual(note_one.content, test_note_content)


class NoteViewTest(TestCase):
    def setUp(self) -> None:
        author = Author.objects.create(name='Test Author')
        Note.objects.create(
            title=test_title, content=test_note_content, author=author)

    def test_note_list_view(self):
        response = self.client.get(reverse('notes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, test_title)

    def test_note_details(self):
        note_one = Note.objects.get(id=1)
        response = self.client.get(
            reverse('note_detail', args=[str(note_one.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, test_title)
        self.assertContains(response, test_note_content)
