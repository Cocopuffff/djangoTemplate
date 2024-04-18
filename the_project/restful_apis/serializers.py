from rest_framework import serializers
from .models import Task

# serialises from db to json and json to db
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # which model / json to look at
        model = Task
        # which fields
        fields = '__all__'
        # fields = ('title', 'completed')  # specify fields you want
        #exclude = ('completed',)  #exclude specific field, one or the other

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('Title has to be at least 5 characters long')

        return value