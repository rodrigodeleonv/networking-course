from django.db import models


class HomeworkDefinition(models.Model):
    name = models.CharField(max_length=50)
    index = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.name


class Homework(models.Model):
    PROCESSED_CHOICE = (
        ('N', 'No Processed'),
        ('P', 'Processing'),
        ('F', 'Finished')
    )
    score = models.PositiveSmallIntegerField(null=True)
    filename = models.FileField(upload_to='homework/')
    processed = models.CharField(max_length=1, choices=PROCESSED_CHOICE, default='N')
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)
    definition = models.ForeignKey(HomeworkDefinition, on_delete=models.CASCADE)

    def __str__(self):
        self.score
