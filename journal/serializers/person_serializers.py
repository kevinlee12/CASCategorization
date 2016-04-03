from rest_framework import serializers
from journal.models import Student, Advisor, Coordinator, School


class StudentSerializer(serializers.ModelSerializer):
    """Student model serializer"""
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'personal_code', 'student_id',
                  'grad_month', 'grad_year', 'advisor', 'coordinator', 'school')


class AdvisorSerializer(serializers.ModelSerializer):
    """Advisor model serializer"""
    class Meta:
        model = Advisor
        fields = ('first_name', 'last_name', 'advisor_type', 'coordinator',
                  'school')


class CoordinatorSerializer(serializers.ModelSerializer):
    """Coordinator model serializer"""
    class Meta:
        model = Coordinator
        fields = ('first_name', 'last_name', 'coordinator_type', 'school')

class SchoolSerializer(serializers.ModelSerializer):
    """School model serializer"""
    class Meta:
        model = School
        field = ('name', 'school_id', 'address', 'city', 'state', 'country')
