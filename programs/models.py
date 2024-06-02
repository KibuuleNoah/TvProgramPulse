from django.db import models
import json
from users.models import CustomUser

# Create your models here.


class Television(models.Model):
    name = models.CharField(max_length=20, unique=True)
    rating = models.FloatField(default=0.0)
    region = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


with open("./genres.json") as f:
    GENRE_CHOICES = json.load(f)


class Program(models.Model):
    name = models.CharField(max_length=50, unique=True)
    rating = models.FloatField(default=0.0)
    time = models.TimeField()
    days = models.TextField()
    genre = models.CharField(max_length=50, null=True, choices=GENRE_CHOICES)
    language = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    television = models.ForeignKey(Television, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def p_days(self):
        if self.days:
            return self.days.split(",")
        return []


class Programs(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}-{self.program.name}"

    class Meta:
        unique_together = ("user", "program")


# class Programs(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     program = models.ForeignKey(Program, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.user.username}-{self.program.name}"
#
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['user', 'program'], name='unique_user_program')
#         ]

# class Programs(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     program = models.ForeignKey(Program, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.user.username}-{self.program.name}"
