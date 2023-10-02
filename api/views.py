from rest_framework import filters,status
from api.models import Banks, EasyView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from api.serializers import BankViewSerializer, BankBranchesSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse



def home(request):
    '''
        Home View
    '''
    data = {
        "instructions" : "Three endpoints",
        "endpoints" : ["/api/get-banks", "api/get-branch-by-ifsc/ifsc",
                       "api/get-branch-by-search?search=<your_search_term"],
        "options" : "fields available for third endpoint - ['branch','city','district','state','bank_name']",
        }
    return JsonResponse(data=data, status=status.HTTP_200_OK)


'''
    NOTE : ALL THE VIEWS ACCEPT ONLY GET REQUESTS AS THESE ARE ONLY RETURNING THE DATA FROM THE DATABASE ACCORDING
    TO THE USER'S REQUEST. NO NEW DATA IS BEING ADDED TO THE DATABASE.THERE ARE THREE TYPES OF REQUESTS AVAILABLE:
    1. Listing all the banks available
    2. Getting the details of a particular branch by providing its IFSC
    3. Getting the branch details by providing any of its attributes like bank name,branch,city etc.
'''
# Create your views here.
class BankListView(ListAPIView):
    """
        A simple view to retrieve all the banks available in the database.
        url : http://localhost:8000/api/get-banks/
    """
    
    queryset = Banks.objects.all()
    serializer_class = BankViewSerializer


class BranchByIfscView(RetrieveAPIView):
    """
        View to retrieve particular branch details if IFSC is provided.
        Eg : 'http://localhost:8000/api/get-branch-by-search/ABHY0065001'
    """
    
    queryset = EasyView.objects.all()
    serializer_class = BankBranchesSerializer
    
    
class BranchesView(ListAPIView):
    """
        View to retrieve branch details based on users search terms and filters.
        Two options are available:
        1. search : User can provide a search term in the 'search' query parameter. Can be used for vague searches
           For example, if user knows the branch as a mumbai branch, but doesnt know its exact value, user can 
           request like this :
           Eg : 'http://localhost:8000/api/get-branch-by-search?search=mumbai'

        2. attribute name : if the user knows the exact attribute value, then it can be provided in query parameter.
           Eg : 'http://localhost:8000/api/get-branch-by-search?branch=GREATER MUMBAI'
        Avaialable fields are : bank_name, branch, city, district, state. Can combine search terms.
    """

    queryset = EasyView.objects.all()
    serializer_class = BankBranchesSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['branch','city','district','state','bank_name']
    filterset_fields = ['branch','city','district','state','bank_name']

