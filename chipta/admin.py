from django.contrib import admin
import random
import datetime
from faker import Faker
from django.http import HttpRequest
from chipta.models import *
# Register your models here.
faker = Faker()


class ChiptaAdmin(admin.ModelAdmin):
    date_time_ = faker.date_time()
    arrival_time = date_time_ + datetime.timedelta(days=2)

    def get_changeform_initial_data(self, request: HttpRequest) -> dict[str, str]:
        return {"raqam" : random.randint(1000000000, 9999999999),
                "kompaniya": faker.company(),
                "ketish_vaqti": self.date_time_,
                "kelish_vaqti": self.arrival_time,
                "qaysi_shaharga": faker.city(),
                "qaysi_shahardan": faker.city(),
                "soni": 47
                }
    list_display = ['id', 'raqam', 'kompaniya', 'ketish_vaqti', 'kelish_vaqti', 'qaysi_shaharga', 'qaysi_shahardan', 'soni']
    ordering = ['id', 'kompaniya', 'ketish_vaqti', 'kelish_vaqti', 'qaysi_shaharga', 'qaysi_shahardan']
    list_editable = ['kompaniya', 'ketish_vaqti', 'kelish_vaqti', 'qaysi_shaharga', 'qaysi_shahardan']
    list_display_links = ["id", "raqam"]


class YolovchiAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request: HttpRequest) -> dict[str, str]:
        return {
            'ismi': faker.first_name(),
            'sharifi': faker.last_name(),
            'email': faker.email(),
            'telefon': faker.phone_number()
        }

    list_display = ['id', 'ismi', 'sharifi', 'email', 'telefon']
    ordering = ['ismi', 'sharifi', 'email']
    list_editable = ['ismi', 'sharifi', 'email', 'telefon']
    # list_display_links = ['ismi', 'sharifi', 'email', 'telefon']


admin.site.register(Chipta, ChiptaAdmin)
admin.site.register(Yolovchi, YolovchiAdmin)
admin.site.register(Band_qilish)
