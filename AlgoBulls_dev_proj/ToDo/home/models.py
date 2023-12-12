from django.db import models

class Task(models.Model):

    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateTimeField(blank=True, null=True)
    tags = models.TextField(blank=True)  # Storing comma-separated value
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
        
    def set_tags(self, tags_list):
        self.tags = ','.join(tags_list)

    def get_tags(self):
        return self.tags.split(',') if self.tags else []

    def __str__(self):
        return self.title
