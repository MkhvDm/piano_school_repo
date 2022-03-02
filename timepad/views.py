from piano_school import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from timepad.utils import EventCalendar
from .models import Event
from django.utils import timezone
from django.db.models.functions import ExtractMonth


def timepad(request, year, month: int):
    if not request.user.is_authenticated:
        return redirect('account:account')
    month_num = month if month in range(1, 13) else 1  # todo redirect on default_timepad
    next_month_num = (month_num + 1) % 12
    prev_month_num = ((month_num - 1) % 12) if (month_num > 1) else 12
    next_year_num = year + 1 if month_num == 12 else year
    prev_year_num = year - 1 if month_num == 1 else year
    month_str = calendar.month_name[month_num].capitalize()

    user = request.user
    user_pk = request.user.pk
    # get from DB count of lessons on each day:
    if user.is_superuser:
        events = Event.objects.filter(start_time__month=month_num, start_time__year=year)
    else:
        events = Event.objects.filter(student_ids=user_pk, start_time__month=month_num, start_time__year=year)

    event_sum_dict = dict()
    for event in events:
        day = event.start_time.day
        if day in event_sum_dict:
            event_sum_dict.get(day)
            event_sum_dict.update({day: event_sum_dict.get(day) + 1})
        else:
            event_sum_dict.update({day: 1})
    print(event_sum_dict)

    cal = EventCalendar()  # HTMLCalendar
    if settings.SUNDAY_FIRSTWEEKDAY:
        cal.setfirstweekday(6)
    cal = cal.formatmonth(year, month_num, event_sum_dict)  # events_on_day_dict {day: num_of_events}
    now = datetime.now()
    current_year = now.year

    return render(request, 'timepad/timepad.html',
                  {'month_str': month_str,
                   'month_num': month_num,
                   'prev_month_num': prev_month_num,
                   'next_month_num': next_month_num,
                   'year': year,
                   'prev_year_num': prev_year_num,
                   'next_year_num': next_year_num,
                   'cal': cal,
                   'current_year': current_year,
                   })


def timepad_default(request):
    now = datetime.now()
    month = now.month
    year = now.year
    return timepad(request, year, month)


def all_events(request, year, month):
    if not request.user.is_authenticated:
        return redirect('account:account')
    month_num = month
    month_str = calendar.month_name[month].capitalize()
    user = request.user
    user_pk = request.user.pk

    if user.is_superuser:
        events = Event.objects.filter(start_time__month=month_num, start_time__year=year)
    else:
        events = Event.objects.filter(start_time__month=month_num, start_time__year=year, student_ids=user_pk)

    return render(request, 'timepad/events.html', {'events':     events,
                                                   'month_num':  month_num,
                                                   'month_str':  month_str,
                                                   'year':       year,
                                                   })


def date_events(request, year, month, day):
    if not request.user.is_authenticated:
        return redirect('account:account')
    month_num = month
    month_str = calendar.month_name[month_num].capitalize()
    user = request.user
    user_pk = request.user.pk

    date = datetime(year, month_num, day).date()
    if user.is_superuser:
        events = Event.objects.filter(start_time__date=date).order_by('start_time')
    else:
        events = Event.objects.filter(start_time__date=date, student_ids=user_pk).order_by('start_time')
    return render(request, 'timepad/date_events.html', {'year':      year,
                                                        'month_num': month_num,
                                                        'month_str': month_str,
                                                        'day':       day,
                                                        'events':    events})


