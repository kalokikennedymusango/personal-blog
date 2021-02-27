from django.contrib import admin
from . models import update
from . models import aboutus
from . models import Portfolio
from . models import Astroh
from . models import Review
from . models import Contacts

# Register your models here.
admin.site.register(update)
admin.site.register(aboutus)
admin.site.register(Portfolio)
admin.site.register(Astroh)
admin.site.register(Review)
admin.site.register(Contacts)