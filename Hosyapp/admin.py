from django.contrib import admin
from Hosyapp.models import Users
from Hosyapp.models import Product
from Hosyapp.models import Member
from Hosyapp.models import Contact

# Register your models here.
admin.site.register(Users)
admin.site.register(Product)
admin.site.register(Member)
admin.site.register(Contact)
