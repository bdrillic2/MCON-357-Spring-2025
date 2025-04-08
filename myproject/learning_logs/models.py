from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Topics'
        db_table = 'topic'

    def __str__(self):
        return self.name


class Entry(models.Model):
    ## when topic associated with this Entry is deleted all entries associated with it will be deleted
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Entries'
        db_table = 'entry'

    def __str__(self):
        return self.title