from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import viewsets, generics, permissions, pagination
from rest_framework.renderers import JSONRenderer
from restaurant_notes.models import RestaurantNote, Customer
from restaurant_notes.serializers import UserSerializer, GroupSerializer, RestaurantNoteSerializer,  CustomerSerializer, ClientSerializer




class UserViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing user instances.
    author: Mark Ellis
    """
    queryset = User.objects.all().order_by('-date_joined')

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            serializer_class = UserSerializer
            return serializer_class
        else:
            serializer_class = ClientSerializer
            return serializer_class

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    author: Mark Ellis
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing group instances.
    author: Mark Ellis
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class RestaurantNotePagination(pagination.PageNumberPagination):
    page_size = 80  # the no. of company objects you want to send in one go

class RestaurantNoteViewSet(viewsets.ModelViewSet):
	"""
    A ViewSet for viewing and editing restaurant note instances.
    author: Mark Ellis
	"""
	queryset = RestaurantNote.objects.all()
	serializer_class = RestaurantNoteSerializer
	pagination_class = RestaurantNotePagination

def deleteNote(request, pk):
	try:
		note = RestaurantNote.objects.filter(pk=pk)
		note.delete()
	except:
		return JsonResponse({"status": 'error'})
	return JsonResponse({"status": 'success'})