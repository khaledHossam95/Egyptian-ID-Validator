from rest_framework.decorators import api_view , authentication_classes , permission_classes 
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializer import IDCardSerializer,IDOutputSerializer
# Create your views here.



@api_view(["POST"])
@authentication_classes([TokenAuthentication]) #Token for users
@permission_classes([IsAuthenticated | HasAPIKey]) #Both Auth Users OR Anons can use the API.
def CheckID(request):

    id_card = IDCardSerializer(data=request.data)
    id_card.is_valid(raise_exception=True)
    output = id_card.parsed_data
    response = IDOutputSerializer(output)
    return Response(response.data , status = 200)