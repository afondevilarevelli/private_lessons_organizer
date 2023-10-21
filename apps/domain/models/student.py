from django.db import models
import uuid


def student_image_dir_path(instance, filename):
    return f"students/{instance.id}/{filename}"


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    contact_email = models.EmailField(null=True, blank=True)
    image = models.ImageField(
        upload_to=student_image_dir_path, null=True, blank=True)

    owner = models.ForeignKey('authentication.User', on_delete=models.CASCADE)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
