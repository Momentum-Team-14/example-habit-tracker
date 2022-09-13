from rest_framework.views import APIView
from habit_tracker.models import Habit
from rest_framework.response import Response
from .serializers import HabitSerializer


class HabitListView(APIView):
    def get(self, request, format=None):
        """
        Return a json list of all habits
        """
        # first, query for all the things I want to return
        habits = Habit.objects.all()
        # second serialize the data I want to return
        serializer = HabitSerializer(habits, many=True)
        # return the response with the data
        return Response(serializer.data)
