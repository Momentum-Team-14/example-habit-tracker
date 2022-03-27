import datetime
from django import forms
from .models import Habit, DailyRecord


class DatePickerInput(forms.DateInput):
    input_type = "date"


class HabitForm(forms.ModelForm):
    # https://docs.djangoproject.com/en/4.0/ref/forms/widgets/#styling-widget-instances-1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "input"})
        self.fields["goal"].widget.attrs.update({"class": "input"})

    class Meta:
        model = Habit
        fields = ("name", "goal")
        labels = {
            "name": "What habit do you want to build?",
            "goal": "What is your target number for daily reps of this habit?",
        }


class DailyRecordForm(forms.ModelForm):
    habit_pk = forms.IntegerField(widget=forms.HiddenInput(), required=False, label="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["result"].widget.attrs.update({"class": "input"})
        self.fields["date"].widget.attrs.update({"class": "input"})

    class Meta:
        model = DailyRecord
        fields = ("date", "result", "habit_pk")
        widgets = {"date": DatePickerInput()}
