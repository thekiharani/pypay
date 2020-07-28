from django.db import models
from django.utils.translation import ugettext_lazy as _

class Note(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='No content yet...')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "geeky_notes"
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")
        ordering = ['-created_at']

    def __str__(self):
        return self.title
