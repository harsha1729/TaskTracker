from django.db import models

class Task(models.Model):

    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in-progress', 'In Progress'),
        ('done', 'Done')
    ]
    title = models.CharField(max_length=50) 
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Task: {self.title} Description: {self.description} Status: {self.status}"
