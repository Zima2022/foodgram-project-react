from djoser.views import UserViewSet

from api.pagination import CustomPagination
from api.serializers import UserSerializer
from users.models import User


class UserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
