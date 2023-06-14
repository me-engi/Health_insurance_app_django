from rest_framework import serializers
from .models import InsuranceHolder, FamilyMember

class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = ['name', 'age', 'sex', 'description']

class InsuranceHolderSerializer(serializers.ModelSerializer):
    family_members = FamilyMemberSerializer(many=True, read_only=True)

    class Meta:
        model = InsuranceHolder
        fields = ['id', 'full_name', 'age', 'sex', 'phone_number', 'address', 'description', 'family_members']
