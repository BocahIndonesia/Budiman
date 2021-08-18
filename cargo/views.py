from django.shortcuts import render
from django.http import HttpResponse
#from . import models
# Create your views here.

def index(request):
	return HttpResponse("Halaman home, ada pilihan login dan about")

def login(request):
	return HttpResponse("Halaman ini harus berisi form login dan form daftar")

def validasi(request, username, password):
	try:
		akun=Akun.objects.get(username=username)
		if akun.
	except:
		login(request)
	
def superadmin(request):
	pass

def admin(request):
	pass

def adminagen(request):
	pass

def konsumen(reqeust):
	pass

def home(request, id_akun):
	pass
	#if(akun.role==0):
	#	superadmin(request)
	#else if(akun.role==1):
	#	admin(request)
	#else if(akun.role==2):
	#	adminagen(request)
	#else if(akun.role==3):
	#	konsumen(request)
