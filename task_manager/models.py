from django.db import models


# Represents a Sticky Note
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        'Author', on_delete=models.CASCADE, null=True, blank=True)


# Holds the Author of the Sticky Note
class Author(models.Model):
    name = models.CharField(max_length=255)
