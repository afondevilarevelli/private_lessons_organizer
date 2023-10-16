from django.db import models
import uuid


class LessonItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.DateTimeField(max_length=300)
    completed = models.BooleanField(default=False)

    lesson = models.ForeignKey(
        'Lesson', on_delete=models.CASCADE, related_name='lesson_items')
