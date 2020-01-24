from .forex import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_forex_rate_view(request, *args, **kwargs):
    try:
        data = request.data
        # print(data)
        if data['base_cur'] == data['dest_cur']:
            return Response({"Base and destination currency must be different!"}, status=400)        
        result = forex_rate(data['base_cur'], data['dest_cur'])
        # print(result)
        if result == 'apidown' or result == '404':
            return Response({result}, status=404)
        return Response({"converted_amount": result * float(data["amount"]), "exchange_rate": result}, status=200)
    except:
        return Response({"Something went wrong. Please try again later."}, status=404)

#     {
# "base_cu": "INR",
# "dest_cur": "INR",
# "amount":2000
# }
