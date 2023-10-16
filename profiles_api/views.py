from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from profiles_api.models import UserProfile, ProfileFeedItem
from profiles_api.serializer import UserSerializer, ProfileFeedSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.settings import api_settings


# Create your views here.
class HelloApiView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        """return a list of apiview"""

        user = UserProfile.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        # create new user.
        try:
            name = request.POST["name"]
            email = request.POST["email"]
            member = UserProfile(name=name, email=email)
            member.save()
            return Response("successfully created user")
        except Exception as exc:
            print("Error in filling seed data from blob.", str(exc))

    def put(self, request):
        try:
            # update user name for given email.
            email = request.POST["email"]
            name = request.POST["name"]
            mydata = UserProfile.objects.get(email=email)
            UserProfile.objects.filter(email=email).update(name=name)

            return Response("successfully updated user")
        except Exception as exc:
            print("Error in filling seed data from blob.", str(exc))


# NOTE- Test ViewSet
class APIViewSet(viewsets.ViewSet):
    """testing viewset"""

    def list(self, request):
        a_viewset = ["a", "b", "c", "d"]
        return Response({"message": "Hello!", "a_viewset": a_viewset})


class UserLoginApiView(ObtainAuthToken):
    """handle creating user auth token"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedSerializer
    queryset = ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        "set the user profile to the logged in user"
        serializer.save(user_profile=self.request.user)
