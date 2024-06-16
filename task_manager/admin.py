from django.contrib import admin
from .models import Note
from .models import Author

# Register models for the Note and Author

admin.site.register(Note)

admin.site.register(Author)
