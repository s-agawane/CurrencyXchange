from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import walletSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_balance_view(request, *args, **kwargs):
    try:
        qs = User.objects.filter(username=request.user)[0].profile
        serializer = walletSerializer(qs)
        return Response(serializer.data, status=200)
    except:
        return Response({"Something went wrong. Please try again later."}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deposit_balance_view(request, *args, **kwargs):
    try:
        amount_to_deposit = float(request.data.get("amount"))
        if amount_to_deposit < 0.0 :
            return Response({"Amount invalid!"}, status=400)
        qs = User.objects.filter(username=request.user)[0].profile
        # print(request.data, qs.balance)
        
        qs.balance = qs.balance + amount_to_deposit
        qs.save()
        return Response({"Deposit successful."}, status=200)
    except Exception as e:
        print(e)
        return Response({"Something went wrong. Please try again later."}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def withdraw_balance_view(request, *args, **kwargs):
    try:
        qs = User.objects.filter(username=request.user)[0].profile
        # print(request.data, qs.balance)
        amount_to_withdraw = float(request.data.get("amount"))
        if amount_to_withdraw < 0.0 :
            return Response({"Amount invalid!"}, status=400)
        if amount_to_withdraw > qs.balance:
            return Response({"Insufficient Balance. Please add funds!!"}, status=400)
        qs.balance = qs.balance - amount_to_withdraw
        qs.save()
        return Response({"Withdraw successful."}, status=200)
    except Exception as e:
        print(e)
        return Response({"Something went wrong. Please try again later."}, status=404)