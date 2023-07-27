# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, FavoriteQuestion, ReadQuestion
from ..questionmanagement.v1.serializers import UserCountSerializer


@api_view(['GET'])
def user_favorite_read_count(request):
    users = User.objects.all()
    data = []
    for user in users:
        favorite_count = FavoriteQuestion.objects.filter(user_id=user.id).count()
        read_count = ReadQuestion.objects.filter(user_id=user.id).count()
        data.append({
            'user_id': user.id,
            'favorite_count': favorite_count,
            'read_count': read_count,
        })
    return Response(UserCountSerializer(data, many=True).data)
