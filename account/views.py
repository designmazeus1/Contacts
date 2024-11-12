from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

# Bu yerda models dagi modellar
from .models import (
    User,
    ProfileFeedItem,
)

# Bu yerda permissions dagi malumotlar
from .permissions import (
    UpdateOwnProfile,
    PostOwnStatus
)

# Bu yerda serializers dagi malumotlar
from .serializers import (
    HelloSerializer,
    UserProfileSerializer,
    ProfileFeedItemSerializer,
)


class HelloApiView(APIView):
    """ API ko'rinishini sinovdan o'tkazish."""

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """APIView xususiyatlari ro‘yxatini qaytaradi."""

        an_apiview = [
            'HTTP usullarini funksiya sifatida ishlatadi (olish, joylashtirish, tuzatish, qoyish, ochirish',
            "Bu an'anaviy Django ko'rinishiga o'xshaydi",
            "Sizga mantiqingiz ustidan eng ko'p nazoratni beradi",
            "URL manzillariga qo'lda ko'rsatilgan"
        ]

        return Response({'message': 'Salom !', 'an_apiview': an_apiview})

    def post(self, request):
        """Bizning ismimiz bilan salomlashish xabarini yarating."""

        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f"Salom {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Obyektni yangilash bilan shug'ullanadi."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Yamoq so'rovi faqat so'rovda ko'rsatilgan yangilanishlar maydoni."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Obyektni o'chiradi."""

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ko'rish to'plami."""

    def list(self, request):
        """Salom xabarini qaytarish"""

        a_viewset = [
            'Harakatlardan foydalanadi (roʻyxat, yaratish, olish, yangilash, qisman_yangilash',
            "Marshrutizatorlar yordamida URL-manzillarni avtomatik ravishda xaritalash",
            "Kamroq kod bilan ko'proq funksionallikni ta'minlaydi"
        ]

        return Response({'message': 'Salom !', 'a_viewset': a_viewset})

    def create(self, request):
        """Yangi salom xabarini yarating."""

        serializer = HelloSerializer

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f"Salom {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Obyektni identifikatori bo‘yicha olish bilan shug‘ullanadi."""

        serializer = HelloSerializer(data=request.data)

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Obyektni yangilash bilan shug'ullanadi."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Obyekt qismini yangilash bilan shug'ullanadi"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Ob'ektni olib tashlash uchun qo'llar"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Profil yaratish va yangilash bilan shug'ullanadi"""

    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'email')


class LoginViewSet(viewsets.ViewSet):
    """ Elektron pochta va parolni tekshiradi va autentifikatsiya belgisini qaytaradi."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Tokenni tasdiqlash va yaratish uchun ObtainAuthToken APIView-dan foydalaning."""

        return ObtainAuthToken().as_view()(request=request._request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Profil tasmasini yaratish, o‘qish va yangilash bilan shug‘ullanadi."""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, PostOwnStatus)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """Foydalanuvchi profilini tizimga kirgan foydalanuvchiga o'rnatadi."""
        serializer.save(user_profile=self.request.user)