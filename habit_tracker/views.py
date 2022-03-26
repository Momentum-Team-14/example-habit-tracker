from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import HabitForm


@login_required
def habit_list(request):
    habits = request.user.habits.all()
    return render(
        request,
        "habit_tracker/habit_list.html",
        {"habits": habits, "form": HabitForm()},
    )


def habit_new(request):
    if request.method == "POST":
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect("habit_list")

    return render(request, "habit_tracker/habit_new.html", {"form": HabitForm()})
