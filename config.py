import time
# token
BOT_TOKEN = "BOT TOKEN"
# main func
class Data:
    def __init__(self):
        self.message_about_today = f"Сегодня {time.localtime().tm_mday}, Месяц: {time.localtime().tm_mon}"
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
        self.next_day_location = time.localtime().tm_mday + 2

