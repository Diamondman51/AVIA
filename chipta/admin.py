import datetime

from django.contrib import admin
# Register your models here.
from faker import Faker

from chipta.models import Chipta, Yolovchi, Band_qilish

fake: Faker = Faker()


class ChiptaAdmin(admin.ModelAdmin):

    def get_changeform_initial_data(self, request):
        f_date = fake.date_time()
        # t_date = datetime.datetime(f_date.year, f_date.month, f_date.day, f_date.hour, f_date.minute)
        t_date = f_date
        s_date = t_date + datetime.timedelta(hours=2)
        return {
            'raqam': fake.random_int(1000000000, 9999999999),
            'kompaniya': fake.company(),
            'ketish_vaqti': t_date,
            'kelish_vaqti': s_date,
            'qaysi_shaharga': fake.city(),
            'qaysi_shahardan': fake.city(),
        }

    def save_model(self, request, obj, form, change):
        obj.ketish_vaqti = datetime.datetime(obj.ketish_vaqti.year, obj.ketish_vaqti.month, obj.ketish_vaqti.day, obj.ketish_vaqti.hour, obj.ketish_vaqti.minute)
        return super().save_model(self, obj, form, change)

    list_display = ['id', 'raqam', 'kompaniya', 'is_reserved', 'ketish_vaqti', 'kelish_vaqti', 'qaysi_shaharga', 'qaysi_shahardan']


class YolovchiAdmin(admin.ModelAdmin):

    def get_changeform_initial_data(self, request):
        return {
            'ismi': fake.first_name(),
            'sharifi': fake.last_name(),
            'email': fake.email(),
            'telefon': fake.basic_phone_number(),
        }

    list_display = ['id', 'ismi', 'sharifi', 'email', 'telefon']


class Band_qilishAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.chipta.is_reserved = True
        obj.chipta.save()
        return super().save_model(self, obj, form, change)

    list_display = ['id', 'yolovchi', 'chipta']


admin.site.register(Chipta, ChiptaAdmin)
admin.site.register(Yolovchi, YolovchiAdmin)
admin.site.register(Band_qilish, Band_qilishAdmin)
