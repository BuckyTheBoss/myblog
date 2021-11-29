import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
django.setup()

from posts.models import *
from django.contrib.auth.models import User

f = Faker()
if Category.objects.count() < 10:
    for num in range(10):
        Category.objects.create(name=f.first_name())


for num in range(10):
    fname = f.first_name()
    lname = f.last_name()
    full_name = fname+lname
    User.objects.create_user(
        username=full_name,
        email=f'{full_name}@example.com',
        password='Sailboat23',
        first_name=fname,
        last_name=lname
    )