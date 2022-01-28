from rest_framework import serializers


my_default_errors = {
    'required': 'This attribute is required',
    'invalid': '',
    'valid': ''
}


class SerializerAPI(serializers.Serializer):
    city = serializers.CharField(error_messages=my_default_errors)
    temp_format = serializers.ChoiceField(choices=["C", "F"], error_messages=my_default_errors)


