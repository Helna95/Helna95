from rest_framework import serializers
from .models import User, Contact

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'surname', 'image')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        # fields = ('mobile_number', 'email_address', 'res_address')
        fields = '__all__'
        depth = 1