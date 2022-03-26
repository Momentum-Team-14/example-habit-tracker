from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def habit_list(request):
    habits = request.user.habits.all()

    return render(request, "habit_tracker/habit_list.html", {"habits": habits})
