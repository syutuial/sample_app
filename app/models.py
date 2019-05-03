from django.db import models

class Task(models.Model):
    name = models.CharField('task_name', max_length=255)
    created_date = models.DateTimeField('created_date', auto_now_add=True)
    update_date = models.DateTimeField('update_date', auto_now=True)


    def __str__(self):
        return self.name
