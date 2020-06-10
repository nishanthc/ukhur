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
    text = models.TextField(
        blank=True,
        null=True
    )

    word_occurrences_count = JSONField()

    word_occurrences_sentence = JSONField()
