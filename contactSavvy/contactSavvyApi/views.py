from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, ContactSerializer
from .models import User, Contact
# Create your views here.


class ContactList(APIView):

    def get(self, request):
        allContacts = Contact.objects.all()#.order_by('user_id')
        serializer = ContactSerializer(allContacts, many=True)
        print(f"Query contact resultset -------- > {serializer.data}")
        return Response(serializer.data)
    
    def post(self, request,  format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        snippet = Contact.objects.filter(pk=pk).first()
        print(f"Query contact resultset snippet -------- > {snippet}")
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        employee = Contact.objects.filter(pk=pk).first()
        employee.delete()
        return Response({"Success":True, "message":"Contact deleted successfully"}, status=204)

class UsersList(APIView):

    def get(self, request):
        allUsers = User.objects.all()#.order_by('user_id')
        serializer = UserSerializer(allUsers, many=True)
        print(f"Query users resultset -------- > {serializer.data}")
        return Response(serializer.data)
    
    

    def delete(self):
        pass

    def put(self):
        pass

'''
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()#.order_by('user_id')
    print(queryset)
    serializer_class = ContactSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()#.order_by('user_id')
    print(f"Query resultset -------- > {queryset}")
    serializer_class = UserSerializer
'''