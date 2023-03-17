import time
# token
BOT_TOKEN = "6276241260:AAFJjMCgU6P-giS8ni4BIGxNA9Kk9pM8Wuo"
# main func


class Data:
    def __init__(self):
        self.get_time()

    def get_time(self):
        months = {
            1: 'Январь',
            2: 'Февраль',
            3: 'Март',
            4: 'Апрель',
            5: 'Май',
            6: 'Июнь',
            7: 'Июль',
            8: 'Август',
            9: 'Сентябрь',
            10: 'Октябрь',
            11: 'Ноябрь',
            12: 'Декабрь'
        }
        weekdays = {

            1: 'Понедельник',
            2: 'Вторник',
            3: 'Среда',
            4: 'Четверг',
            5: 'Пятница',
            6: 'Суббота',
            7: 'Воскресенье',
        }

        self.this_month = f"{months[time.localtime().tm_mon]}"
        self.this_month_location = time.localtime().tm_mon
        if time.localtime().tm_mon == 12:
            self.next_month = f"{months[1]}"
        self.next_month = f"{months[time.localtime().tm_mon + 1]}"
        self.next_month_location = time.localtime().tm_mon + 1
        if time.localtime().tm_wday == 6:
            self.this_day = weekdays[7]
            self.this_day_location = 7
            self.next_day = weekdays[1]
            self.next_day_location = 1

        self.this_day = weekdays[time.localtime().tm_wday + 1]
        self.this_day_location = time.localtime().tm_wday + 1
        self.next_day = weekdays[time.localtime().tm_wday + 2]
        self.next_day_location = time.localtime().tm_wday + 2

    def isLesson(self, x, y):
        from datetime import time, datetime
        # x_time = time(9, 0, 0)
        # y_time = time(12, 0, 0)
        current_time = datetime.now().time()
        if x <= current_time <= y:
            return True
        return False

    def getRemaining(self, y):
        from datetime import time, datetime
        current_time = datetime.now().time()
        if current_time <= y:
            remaining_minutes = datetime.combine(datetime.today(), y) - datetime.combine(datetime.today(), current_time)
            remaining_minutes = remaining_minutes.total_seconds() // 60
            return remaining_minutes

    def getLesson(self):
        from datetime import time
        text = f"Пара: "
        if Data().isLesson(time(8, 0, 0), time(9, 30, 0)):
            text += f"1\nДо перемены: {Data().getRemaining(time(9, 30, 0))} мин"
        elif Data().isLesson(time(9, 40, 0), time(11, 10, 0)):
            text += f"2\nДо перемены: {Data().getRemaining(time(11, 10, 0))} мин"
        elif Data().isLesson(time(11, 30, 0), time(13, 0, 0)):
            text += f"3\nДо перемены: {Data().getRemaining(time(13, 0, 0))} мин"
        elif Data().isLesson(time(14, 0, 0), time(15, 30, 0)):
            text += f"4\nДо перемены: {Data().getRemaining(time(15, 30, 0))} мин"
        elif Data().isLesson(time(15, 40, 0), time(17, 10, 0)):
            text += f"5\nДо перемены: {Data().getRemaining(time(17, 10, 0))} мин"
        elif Data().isLesson(time(17, 20, 0), time(18, 50, 0)):
            text += f"6\nДо перемены: {Data().getRemaining(time(18, 50, 0))} мин"
        else:
            text = "Перемена либо домой сьебобо"
        return text
