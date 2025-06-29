from rest_framework import serializers
from .models import *

class MainserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mainservice
        fields =('main_service_name',)

class SubserviceSerializer(serializers.ModelSerializer):
    main_service_name = MainserviceSerializer()
    class Meta:
        model = Subservicename
        fields = ('id','main_service_name','service_name', 'service_img','about_service')

class EnquiriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiries
        fields = '__all__'