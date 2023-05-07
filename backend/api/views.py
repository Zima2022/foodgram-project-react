from djoser.views import UserViewSet
from rest_framework import viewsets

from api.filters import IngredientFilter
from api.pagination import CustomPagination
from api.permissions import IsAdminOrReadOnly
from api.serializers import IngredientSerializer, TagSerializer, UserSerializer
from recipes.models import Ingredient, Tag
from users.models import User


class UserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (IngredientFilter, )
    search_fields = ('^name', )
    pagination_class = None
