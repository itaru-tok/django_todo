from django.db import models

class TodoItem(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'todo'

    def __str__(self):
        return self.content