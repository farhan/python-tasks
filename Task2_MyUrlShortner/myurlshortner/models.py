from django.db import models


class UrlKey(models.Model):
    key_name = models.CharField(db_index=True, max_length=100, unique=True)
    is_assigned = models.BooleanField(db_index=True, default=False)
    assigned_timestamp = models.DateTimeField(blank=True, null=True)
    assigned_url = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.key_name

    class Meta:
        ordering = ['is_assigned', 'key_name']
        verbose_name = 'Url Key'
        verbose_name_plural = 'Url Keys'
