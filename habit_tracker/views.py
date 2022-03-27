import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import HabitForm, DailyRecordForm
from .models import Habit, DailyRecord


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


def habit_detail(request, habit_pk):
    habit = get_object_or_404(Habit, pk=habit_pk)

    return render(request, "habit_tracker/habit_detail.html", {"habit": habit})


@login_required
def habit_daily_record(request, habit_pk=None, record_pk=None):
    habit_pk_for_lookup = habit_pk or request.POST.get("habit_pk")
    habit = get_object_or_404(Habit, pk=habit_pk_for_lookup)
    view_context = {"habit": habit}
    if request.method == "GET":
        record_date = datetime.date.today()
        daily_record, _ = habit.records.get_or_create(date=record_date)
    else:
        daily_record_instance = DailyRecord.objects.get(pk=record_pk)
        form = DailyRecordForm(data=request.POST, instance=daily_record_instance)
        if form.is_valid():
            daily_record = form.save(commit=False)
            daily_record.habit = habit
            daily_record.save()

    if daily_record:
        date_value_for_form = daily_record.date
    else:
        date_value_for_form = datetime.date.today()
    view_context.update(
        form=DailyRecordForm(
            initial={"date": date_value_for_form, "habit_pk": habit.pk}
        ),
        daily_record=daily_record,
        habit=habit,
    )

    return render(request, "habit_tracker/habit_results.html", view_context)
