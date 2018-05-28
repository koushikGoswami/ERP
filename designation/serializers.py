from designation.models import Designation
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from company.serializers import CompanyListSerializer
from departments.serializers import DepartmentsListSerializer
from authentication.serializers import UserLoginSerializer,UserReadSerializer

class DesignationSerializer(ModelSerializer):

    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)
    queryset = Designation.objects.all()
    class Meta:
        model = Designation
        fields = ['id','company','departments','designation_name','created_at','created_by','status']

    def create(self, validated_data):
        designation = Designation.objects.create(**validated_data)
        return designation

    def update(self, instance, validated_data):
        instance.company = validated_data.get('company', instance.status)
        instance.departments = validated_data.get('departments', instance.status)
        instance.designation_name = validated_data.get('designation_name', instance.status)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class DesignationReadSerializer(ModelSerializer):

    created_by = UserReadSerializer()
    company = CompanyListSerializer()
    departments = DepartmentsListSerializer()
    status = serializers.BooleanField(default=True)

    class Meta:
        model = Designation
        fields = ['id','company','departments','designation_name','created_at','created_by','status']



class  DesignationListSerializer(ModelSerializer):
    class Meta:
        model =  Designation
        fields = ['id','designation_name']