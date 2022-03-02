from calendar import HTMLCalendar
from calendar import day_name, day_abbr


class EventCalendar(HTMLCalendar):

    cssclasses = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    cssclasses_weekday_head = cssclasses
    
    def __init__(self):
        super(EventCalendar, self).__init__()

    def formatweekday(self, day):
        """
        Return a weekday name as a table header.
        """
        return '<th class="%s">%s</th>' % (
            self.cssclasses_weekday_head[day], day_name[day])

    # def formatweekday(self, day):
    #     """
    #     Return a weekday name as a table header.
    #     """
    #     return '<th class="%s">%s</th>' % (
    #         self.cssclasses_weekday_head[day], day_abbr[day])

    def formatday_with_link(self, day, weekday, year, month, event_sum_dict={}):
        """
        Return a day as a table cell.
        """
        if day == 0:
            # day outside month
            return '<td class="%s">&nbsp;</td>' % self.cssclass_noday
        else:
            if day in event_sum_dict.keys():
                event_quantity = event_sum_dict.get(day)
                return '<td class="%s"> <a href="/timepad/events/%d/%d/%d/">' \
                       ' %d <br> lessons: %d ' \
                       '</a></td>' % (self.cssclasses[weekday], year, month, day, day, event_quantity)
            else:
                return '<td class="%s"> <a href="/timepad/events/%d/%d/%d/"> %d </a></td>' % (self.cssclasses[weekday], year, month, day, day)

    def formatweek_with_links(self, theweek, theyear, themonth, event_sum_dict={}):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday_with_link(d, wd, theyear, themonth, event_sum_dict) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatmonth(self, theyear, themonth, event_sum_dict={}, withyear=True):
        """
        Return a formatted month as a table.
        """
        v = []
        a = v.append
        a('<table border="1" cellpadding="0" cellspacing="0" class="%s">' % (
            self.cssclass_month))
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek_with_links(week, theyear, themonth, event_sum_dict))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)




