from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.db.models import Case, CharField, Value, When, IntegerField,Sum,JSONField

class Userlisting(APIView):
	def get(self,request):
		user_data = User.objects.values()
		activity = Activities.objects.values()
		context={
			"user_data":user_data,
			"activity":activity
		}
		return Response(context)