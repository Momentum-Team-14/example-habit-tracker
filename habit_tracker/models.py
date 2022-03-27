from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, BaseModel):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User {self.username} pk={self.pk}"


class Habit(BaseModel):
    name = models.CharField(max_length=255)
    goal = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Habit {self.name} pk={self.pk}>"


class DailyRecord(BaseModel):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="records")
    result = models.PositiveSmallIntegerField(null=True, blank=True)
    date = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["date", "habit"], name="unique_for_habit_and_date"
            )
        ]

    def __str__(self):
        return f"Record for {self.habit.name}: {self.result} on {str(self.date)}"

    def __repr__(self):
        return f"<Record for {self.habit.name} pk={self.pk}>"
