import uuid as uuid
from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.


class Report(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    word_occurrences_count = JSONField()


class Document(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    file_name = models.CharField(
        max_length=300,
    )

    text = models.TextField(
        blank=True,
        null=True
    )

    word_occurrences_count = JSONField()

    word_occurrences_sentence = JSONField()