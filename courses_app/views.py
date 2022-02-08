from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status  # HTTP STATUSES
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

# Login Authentication imports
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# is auth or read only
from rest_framework.permissions import IsAuthenticated


# to be able to search well
from rest_framework import filters

from courses_app import serializers, models
# from courses_app import permissions


class RegisterView(APIView):

    # guarantees the form of data inside
    serializer_class = serializers.UserProfileSerializer
    # def get(self, request, format=None):
    #         'returns a list or dict contains data'
    #         an_apiview = [
    #             'mofty',
    #             'hazem',
    #             'zooma',
    #             'zoooomzom'
    #         ]

    #         return Response({'message': 'Hello', 'an_apiview': an_apiview})
    def post(self, request):
        """Register a new account"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            serializer.create(serializer.validated_data)

            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class CoursesView(APIView):

    # guarantees the form of data inside
    serializer_class = serializers.CourseSerializer

    def get(self, request, format=None):
        'returns a list or dict contains data'
        an_apiview = [
            {
                'Course 1': {"Name": "Lol1", "Details": "This is a lol course provided by mofty"},
                'Course 2': {"Name": "Maths", "Details": "This is a Math course provided by mofty"},
                'Course 3': {"Name": "Science", "Details": "This is a Science course provided by mofty"},

            }

        ]

        return Response({'message': 'Hello', 'courseeeees': an_apiview})

    def post(self, request):
        """Register a new account"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            # serializer.create(serializer.validated_data)
            serializer.save()

            message = f'Course {name} Added'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class CategoriesView(APIView):

    # guarantees the form of data inside
    serializer_class = serializers.CategorySerializer

    def get(self, request, format=None):
        'returns a list or dict contains data'
        category_view = [
            "Welcome to Category Section"
        ]

        return Response({'message': 'Hello', 'Category': category_view})

    def post(self, request):
        """Register a new account"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            # serializer.create(serializer.validated_data)

            message = f'Category {name} Added'
            serializer.save()
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
class ArticlesView(APIView):

    # guarantees the form of data inside
    serializer_class = serializers.ArticleSerializer

    def get(self, request, format=None):
        'returns a list or dict contains data'
        Article_view = [
            "Welcome to Article Section"
        ]

        return Response({'message': 'Hello', 'Article': Article_view})

    def post(self, request):
        """Register a new account"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            # serializer.create(serializer.validated_data)

            message = f'Article {title} Added'
            serializer.save()
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
class PartnersView(APIView):

    # guarantees the form of data inside
    serializer_class = serializers.PartnerSerializer

    def get(self, request, format=None):
        'returns a list or dict contains data'
        Partner_view = [
            "Welcome to Partner Section"
        ]

        return Response({'message': 'Hello', 'Partner': Partner_view})

    def post(self, request):
        """Register a new account"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            # serializer.create(serializer.validated_data)

            message = f'Article {name} Added'
            serializer.save()
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class UserLoginApiView(ObtainAuthToken):
    """handle creating auth tokens for user"""

    # ADD renderer to obtainauthtoken to be able to view it
    # it existed by default in modelviewset but not here
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class CourseViewSet(viewsets.ModelViewSet):
    """Handling Course List"""

    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all()

    # searching
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'details', 'price')


class CategoryViewSet(viewsets.ModelViewSet):
    """Handling Category List"""

    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

    # searching
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name')

class ArticleViewSet(viewsets.ModelViewSet):
    """Handling Article List"""

    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()

    # searching
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title','body')
    
class PartnerViewSet(viewsets.ModelViewSet):
    """Handling Partner List"""

    serializer_class = serializers.PartnerSerializer
    queryset = models.Partner.objects.all()

    # searching
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name')
