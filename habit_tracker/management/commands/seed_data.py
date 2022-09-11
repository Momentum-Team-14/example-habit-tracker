import random
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.hashers import make_password
from habit_tracker.models import Habit, User
from tracker import settings


class Command(BaseCommand):
    help = "Create some data for development"

    def handle(self, *args, **options):
        if settings.DEBUG:
            password = make_password("badpassword")
            user, _ = User.objects.get_or_create(
                username="Belletrix", password=password
            )

            habits = [
                "Naps",
                "Bark at delivery trucks",
                "Catch the tennis ball",
                "Take long walks",
                "Make new friends",
            ]

            for habit in habits:
                Habit.objects.get_or_create(
                    name=habit, goal=random.choice(range(1, 10)), user_id=user.id
                )

            self.stdout.write(self.style.SUCCESS(f"Objects added to database."))

        else:
            raise CommandError("This command only runs when DEBUG is set to True.")
