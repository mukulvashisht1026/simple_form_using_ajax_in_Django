import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTING_MODULE","task2.settings")
django.setup()
application = get_default_application()

