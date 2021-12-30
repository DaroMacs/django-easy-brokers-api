from django.shortcuts import render
from requests.structures import CaseInsensitiveDict
import requests
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey


class UserListView(APIView):
    permission_classes = [HasAPIKey]


# Create your views here.
def index(request):  

    url = "https://api.easybroker.com/v1/properties?page=1&limit=20&search%5Bupdated_after%5D=2020-03-01T23%3A26%3A53.402Z&search%5Bupdated_before%5D=2025-03-01T23%3A26%3A53.402Z&search%5Boperation_type%5D=sale"

    headers = CaseInsensitiveDict()

    headers = {
    "accept": "application/json",
    "X-Authorization": "9es7vjcqdc1le445rz1n40fh9128kj"
    }
    
    response = requests.get(url, headers=headers)
    return render(request, 'index.html',{'response':response})
