from django.contrib import admin


from .models import InsuranceHolder, FamilyMember

admin.site.register(InsuranceHolder)
admin.site.register(FamilyMember)
