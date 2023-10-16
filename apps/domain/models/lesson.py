from django.db import models
import uuid


def lesson_files_dir_path(instance, filename):
    return f"students/{instance.id}/{filename}"


class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.DateTimeField(max_length=300)
    date = models.DateTimeField(max_length=150)
    cancelled = models.BooleanField(default=False)

    student = models.ForeignKey(
        'Student', on_delete=models.CASCADE, related_name='lessons')
    homework = models.OneToOneField(
        'Homework', on_delete=models.CASCADE, related_name="lesson")
