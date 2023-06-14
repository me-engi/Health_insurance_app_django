from django.urls import path
from . import views
from .views import AddInsuranceHolderView, AddFamilyMemberView, SearchInsuranceHoldersView

app_name = 'insurance_app'

urlpatterns = [
    path('add-insurance-holder/', views.add_insurance_holder, name='add_insurance_holder'),
    path('add-family-member/<int:insurance_holder_id>/', views.add_family_member, name='add_family_member'),
    path('search-insurance-holders/', views.search_insurance_holders, name='search_insurance_holders'),
    
]
