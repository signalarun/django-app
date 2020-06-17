from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    return render(request, 'listings/listings.html')

def listing(request):
    return render(request, 'listings/listing.html')