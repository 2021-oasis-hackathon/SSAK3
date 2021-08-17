import csv
import os
import django
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baroProject.settings")
django.setup()

from ownerApp.models import Product, Store
from django.contrib.auth.models import User


CSV_PATH ="dummyProduct4.csv"


count = 1
with open(CSV_PATH, newline='', encoding='utf-8-sig') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:

        if row['category'] == "과일":
            store_pk = 1
        elif row['category'] == "채소/야채":
            store_pk = 2
        elif row['category'] == "곡류":
            store_pk = 3
        else:
            print("카테고리 오류")
            store_pk = 4 #test

        Product.objects.create(
            store = Store.objects.get(pk = store_pk),
            name = row['name'],
            price = row['price'],
            intro = row['intro'],
            Thumbnail=None,
            introImage = None,
            salesRate = row['SUM'],
            category = row['category'],
            expect = row['expect'],
            amount="10kg",
            expectD1=datetime.datetime.strptime("2021-09-06","%Y-%m-%d"),
            expectD2=datetime.datetime.strptime("2021-09-10","%Y-%m-%d"),
            deliveryD1=datetime.datetime.strptime("2021-09-13","%Y-%m-%d"),
            deliveryD2=datetime.datetime.strptime("2021-09-17","%Y-%m-%d"),
            deliveryOption=row['deliveryOption'],
            region=row['region'],

            #숫자들
            age1_M_B = row['age1_M_B'],
            age1_M_W = row['age1_M_W'],
            age1_M_G = row['age1_M_G'],
            age1_W_B = row['age1_W_B'],
            age1_W_W = row['age1_W_W'],
            age1_W_G = row['age1_W_G'],

            age2_M_B = row['age2_M_B'],
            age2_M_W = row['age2_M_W'],
            age2_M_G = row['age2_M_G'],
            age2_W_B = row['age2_W_B'],
            age2_W_W = row['age2_W_W'],
            age2_W_G = row['age2_W_G'],

            age3_M_B = row['age3_M_B'],
            age3_M_W = row['age3_M_W'],
            age3_M_G = row['age3_M_G'],
            age3_W_B = row['age3_W_B'],
            age3_W_W = row['age3_W_W'],
            age3_W_G = row['age3_W_G'],

            age4_M_B = row['age4_M_B'],
            age4_M_W = row['age4_M_W'],
            age4_M_G = row['age4_M_G'],
            age4_W_B = row['age4_W_B'],
            age4_W_W = row['age4_W_W'],
            age4_W_G = row['age4_W_G'],
        )
        

        count += 1
        if count % 10 == 0:
            print(count)

print(count)
print('product dummy DB update end')
