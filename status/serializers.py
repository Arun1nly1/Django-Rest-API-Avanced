from rest_framework import serializers
from .models import Status


'''
Serializers=>JSON
Serializers=>can validate data too
'''

'''
We can create CustomSerializer without model also like here'''

# class CustomSerializer(serializers.Serializer):
#     content = serializers.TextField(max_length=500)



class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
                'content',
                     'image']

        read_only_fields = ['user'] #Read only field


    # def validate_content(self, value):
    #     if len(value) >100000:
    #         raise serializers.ValidationError("This is too long content")
    #     return value

    def validate(self,data):
        content = data.get('content', None)
        if content == '':
            content = None
        image = data.get("image",None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or Image is required")
        return data  


    
            

