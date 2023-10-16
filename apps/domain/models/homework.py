from django.db import models
import uuid


class Homework(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.DateTimeField(max_length=300)

    @property
    def completed(self):
        return all(self.homework_items.values_list("completed", flat=True))
