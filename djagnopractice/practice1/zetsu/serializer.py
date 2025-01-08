from rest_framework import serializers
from.models import Donguha

class Regserializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=5,max_length=10,write_only=True)
    username = serializers.CharField(required=True)
    firstname = serializers.CharField(required=True)
    lastname = serializers.CharField(required=True)

    class Meta:
        model = Donguha
        fields = ['username','firstname','lastname','email','fav_character','password']

    def validate(self, data):
        firstname = data.get('firstname','')
        username = data.get('username','')

        if firstname and firstname.isupper():
            raise serializers.ValidationError({'firstname':"This is not your BirthCertificate so could you please write it without full caps??"})

        if not username.isalnum():
            raise serializers.ValidationError({'username':"is it readable? no right so please write it in a way that i can understand :)"})
        return data

    def create(self,validate_data):
        return Donguha.objects.create_user(**validate_data)
