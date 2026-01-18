from rest_framework import serializers

from teach_subject.models import TeacherSubjects, Subjects


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ('id', 'name')

class TeacherSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSubjects
        fields = ('id', 'subject_id', 'teacher_id')