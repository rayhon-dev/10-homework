from django.db import models
from django.shortcuts import reverse


class Note(models.Model):
    note_title = models.CharField(max_length=100)
    content = models.TextField()

    def get_detail_url(self):
        return reverse('notes:note_detail',args=[self.pk] )

    def get_delete_url(self):
        return reverse('notes:note_delete', args=[self.pk])

    def get_update_url(self):
        return reverse('notes:note_update', args=[self.pk])
