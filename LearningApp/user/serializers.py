from rest_framework import serializers
from .models import CustomUser, EnrolledCourse

class UserCountSerializer(serializers.Serializer):
    user_count = serializers.IntegerField()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'phone_number', 'university', 'profile_picture']

class EnrolledCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrolledCourse
        fields = ['id', 'user', 'course_id', 'course_title']