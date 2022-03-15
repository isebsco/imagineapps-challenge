
import requests
import django

from http.client                import responses

from rest_framework             import generics, status, viewsets
from rest_framework.response    import Response

from django.db.models.expressions import RawSQL, OrderBy

from apiConsumerApp.models      import CocoaContract
from apiConsumerApp.serializers import CocoaContractSerializer

class CocoaContractCreationView (generics.ListAPIView):
    """
    A View for consuming API and saving its information in the DB.
    """
    
    serializer_class = CocoaContractSerializer
    
    def get (self, *args, **kwargs):
        """
        Method to request the info to the API, performs a loop to create a list
        and finally save the info via bulk_create.
        """
        url= 'https://rest.imagineapps.co/cocoa-contracts' #url to get the data
        #pull data from third party rest api
        response = requests.get(url)
        info_list=[]
                      
        for d in range(len(response.json())):
            data = response.json()[str(d)]
            info_list.append(CocoaContract(data=data))            
            
        CocoaContract.objects.bulk_create(info_list)
        return Response(status=status.HTTP_201_CREATED)

class CocoaContractListView (generics.ListAPIView):
       
    serializer_class =  CocoaContractSerializer
    def get_queryset(self):
        print(django.VERSION)
        querySet = CocoaContract.objects.all()
        #querySet = CocoaContract.objects.all().order_by(OrderBy(RawSQL("LOWER(data->>%s)", ("Máximo",)), descending=True))
        return querySet