from api.models import User, Note
from api.serializers import UserSerializer, NoteSerializer

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework import viewsets


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class NotesPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'notes.html', context=None)


class UsersPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'users.html', context=None)
    # def getUser(request):
    #     name = 'kader'
    #     return HttpResponse('{ "name":"' + name + '", "age":19, "city":"Turkey" }')


# Viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
