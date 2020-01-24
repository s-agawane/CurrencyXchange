from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser
from .serializers import dpSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser])
def upload_profile_photo(request, *args, **kwargs):
    try:
        serializer = dpSerializer(data=request.data)
        if serializer.is_valid():
            qs = User.objects.filter(username=request.user)[0].profile
            print(request.FILES)
            qs.profile_photo = request.FILES['file']
            qs.save()
            return Response({"Profile picture update successful."}, status=200)
    except Exception as e:
        print(e)
        return Response({"Something went wrong. Please try again later."}, status=404)

