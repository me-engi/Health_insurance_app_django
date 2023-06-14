from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InsuranceHolder, FamilyMember
from .serializers import InsuranceHolderSerializer, FamilyMemberSerializer
from rest_framework.generics import ListAPIView


def add_insurance_holder(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')
        description = request.POST.get('description')

        insurance_holder = InsuranceHolder.objects.create(
            full_name=full_name,
            age=age,
            sex=sex,
            phone_number=phone_number,
            address=address,
            photo=photo,
            description=description
        )

        return JsonResponse({'message': 'Insurance holder added successfully.'})

def add_family_member(request, insurance_holder_id):
    insurance_holder = get_object_or_404(InsuranceHolder, id=insurance_holder_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        description = request.POST.get('description')

        family_member = FamilyMember.objects.create(
            insurance_holder=insurance_holder,
            name=name,
            age=age,
            sex=sex,
            description=description
        )

        return JsonResponse({'message': 'Family member added successfully.'})

def search_insurance_holders(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        insurance_holders = InsuranceHolder.objects.filter(full_name__icontains=query)

        data = []
        for insurance_holder in insurance_holders:
            data.append({
                'id': insurance_holder.id,
                'full_name': insurance_holder.full_name,
                'age': insurance_holder.age,
                'sex': insurance_holder.sex,
                'phone_number': insurance_holder.phone_number,
                'address': insurance_holder.address,
                'photo': insurance_holder.photo.url if insurance_holder.photo else None,
                'description': insurance_holder.description
            })



class AddInsuranceHolderView(ListAPIView):
    def post(self, request):
        serializer = InsuranceHolderSerializer(data=request.data)
        if serializer.is_valid():
            insurance_holder = serializer.save()
            return Response({'message': 'Insurance holder added successfully.'})
        return Response(serializer.errors, status=400)

class AddFamilyMemberView(ListAPIView):
    def post(self, request, insurance_holder_id):
        insurance_holder = InsuranceHolder.objects.get(pk=insurance_holder_id)
        serializer = FamilyMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(insurance_holder=insurance_holder)
            return Response({'message': 'Family member added successfully.'})
        return Response(serializer.errors, status=400)

class SearchInsuranceHoldersView(ListAPIView):
    def get(self, request):
        query = request.GET.get('query', '')
        insurance_holders = InsuranceHolder.objects.filter(full_name__icontains=query)
        serializer = InsuranceHolderSerializer(insurance_holders, many=True)
        return Response({'insurance_holders': serializer.data})
       
