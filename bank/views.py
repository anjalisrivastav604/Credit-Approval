from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
import math

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        approved_limit = round(36 * int(data["monthly_income"]) / 100000) * 100000

        customer = Customer.objects.create(
            first_name=data["first_name"],
            last_name=data["last_name"],
            age=data["age"],
            monthly_income=data["monthly_income"],
            approved_limit=approved_limit,
            phone_number=data["phone_number"]
        )

        return Response({
            "customer_id": customer.id,
            "name": f"{customer.first_name} {customer.last_name}",
            "age": customer.age,
            "monthly_income": customer.monthly_income,
            "approved_limit": customer.approved_limit,
            "phone_number": customer.phone_number
        }, status=status.HTTP_201_CREATED)

