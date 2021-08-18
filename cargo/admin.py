from django.contrib import admin
from .models import Role, Konsumen, Personil, Bus, Admin, Agen
# Register your models here.

admin.site.register(Role)
admin.site.register(Konsumen)
admin.site.register(Personil)
admin.site.register(Bus)
admin.site.register(Admin)
admin.site.register(Agen)
