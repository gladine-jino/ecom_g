from django.test import TestCase
import datetime
# Create your tests here.
start_date_time_obj = datetime.datetime.strptime('2022-12-01', '%Y-%m-%d').date()

print(start_date_time_obj)
print(type(start_date_time_obj))