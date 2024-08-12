from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .serializers import UserSerializer, EducationSerializer, WorkSerializer, ProjectsSerializer
from .models import Education, Work, Projects

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer
  permission_classes = [AllowAny]

class EducationViewSet(viewsets.ModelViewSet):
  queryset = Education.objects.all()
  serializer_class = EducationSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

class WorkViewSet(viewsets.ModelViewSet):
  queryset = Work.objects.all()
  serializer_class = WorkSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

class ProjectsViewSet(viewsets.ModelViewSet):
  queryset = Projects.objects.all()
  serializer_class = ProjectsSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]