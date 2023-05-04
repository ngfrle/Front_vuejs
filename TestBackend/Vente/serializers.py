# import serializers from the REST framework
from rest_framework import serializers
 

from django.contrib.auth.models import User

from rest_framework import serializers, validators
from .models import Restaurant,Commentaire, Produit,Restaurateur



class VenteSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Restaurant
        fields = ('Titre','siege', 'Image','telephone','Email','description','restaurateur')

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model= Commentaire
        fields = ('name2','email2','phone2','suject2','description2')

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model= Produit
        fields =('titre','prix','Restaurant','image','date_ajout')




# serializers.py

from rest_framework import serializers
from .models import Restaurateur

class RestaurateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurateur
        fields = ('username', 'email', 'password', 'phone_number')




from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password', 'phone_number')

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()







# serializers.py

from rest_framework import serializers
from .models import Restaurateur


class RestaurateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurateur
        fields = ["id", "username", "email","password", "phone_number"]


# serializers.py

from rest_framework import serializers
from .models import Client


# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = ["id", "username", "email", "phone_number", "password"]
#         extra_kwargs = {"password": {"write_only": True}}


from rest_framework import serializers
from .models import Client

# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = ('id', 'username', 'email', 'phone_number')
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'username', 'email', 'password', 'phone_number')

    def create(self, validated_data):
        user = Client.objects.create(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()



from rest_framework import serializers
from .models import Produit

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'