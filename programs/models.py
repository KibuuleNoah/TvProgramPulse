from time import strftime
from django.db import models
from datetime import datetime, time as Time
import json
from users.models import CustomUser

# Create your models here.
# from datetime import datetime, timedelta
#
# dt1 = datetime.now()
# dt2 = dt1 + timedelta(days=1, hours=2, minutes=30)
# print(dt2)


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
    duration = models.IntegerField(default=0)
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
            return self.days.split(" ")
        return []

    @staticmethod
    def add_mins_to_time(time: Time, minutes: int):
        h, m = time.hour, time.minute
        t = h * 60 + m + minutes
        h, m = divmod(t, 60)
        h %= 24
        return datetime.strptime(f"{h}:{m}", "%H:%M").time()

    @property
    def get_status(self):
        today = strftime("%a")
        if today in str(self.days):
            program_start_tm = self.time
            # time(hour=16, minute=24)
            program_end_tm = self.add_mins_to_time(program_start_tm, self.duration)
            current_time = datetime.now().time()

            if program_start_tm > current_time:
                return "Upcoming"
            elif program_end_tm < current_time:
                return "Ended"
            return "Ongoing"
        return "NotToday"


class UserPrograms(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}-{self.program.name}"

    class Meta:
        unique_together = ("user", "program")


# class UserPrograms(models.Model):
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

# class UserPrograms(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     program = models.ForeignKey(Program, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.user.username}-{self.program.name}"
