import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
django.setup()

from posts.models import *

f = Faker()
if Category.objects.count() < 10:
    for num in range(10):
        Category.objects.create(name=f.first_name())