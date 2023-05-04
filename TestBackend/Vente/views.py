from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Restaurant,Commentaire, Produit
# , Commentaire
from .serializers import VenteSerializer ,CommentaireSerializer,ProduitSerializer
# , RegisterSerializer
# CommentaireSerializer

class ListRestaurantView(ListAPIView):
    queryset= Restaurant.objects.all()
    serializer_class= VenteSerializer 

class CreateRestaurantView(CreateAPIView):
    queryset= Restaurant.objects.all()
    serializer_class= VenteSerializer 

class UpdateRestaurantView(UpdateAPIView):
    queryset= Restaurant.objects.all()
    serializer_class= VenteSerializer 

class DeleteRestaurantView(DestroyAPIView):
    queryset= Restaurant.objects.all()
    serializer_class= VenteSerializer 


class ListCommentaireView(ListAPIView):
    queryset= Commentaire.objects.all()
    serializer_class= CommentaireSerializer

class CreateCommentaireView(CreateAPIView):
    queryset= Commentaire.objects.all()
    serializer_class= CommentaireSerializer

class ListProduitView(ListAPIView):
    queryset= Produit.objects.all()
    serializer_class= ProduitSerializer

class CreateProduitView(CreateAPIView):
    queryset= Produit.objects.all()
    serializer_class= ProduitSerializer

class UpdateProduitView(UpdateAPIView): 
    queryset= Produit.objects.all()
    serializer_class= ProduitSerializer

class DeleteProduitView(DestroyAPIView):
    queryset= Produit.objects.all()
    serializer_class= ProduitSerializer 






from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurateur

class DeleteRestaurateurView(APIView):
    def delete(self, request, pk):
        try:
            restaurateur = Restaurateur.objects.get(pk=pk)
        except Restaurateur.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        restaurateur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

















# views.py

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurateur
from .serializers import (
    LoginSerializer,
    PasswordResetSerializer,
    RegisterSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = Restaurateur.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if user:
            login(request, user)
            return Response({"detail": "Successfully logged in."})
        else:
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Successfully logged out."})


class PasswordResetView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        user = Restaurateur.objects.filter(email=email).first()
        if user:
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            # Send email with uidb64 and token here
            return Response({"detail": "Password reset email sent."})
        else:
            return Response(
                {"detail": "User with this email does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )
# views.py

from rest_framework import mixins, generics
from .models import Restaurateur
from .serializers import RestaurateurSerializer

class RestaurateurList(mixins.ListModelMixin,
                       generics.GenericAPIView):
    """
    Récupère une liste de tous les restaurateurs enregistrés
    """
    queryset = Restaurateur.objects.all()
    serializer_class = RestaurateurSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



# views.py










# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Client
# from .serializers import ClientSerializer

# @api_view(['POST'])
# def Clientregister(request):
#     serializer = ClientSerializer(data=request.data)
#     if serializer.is_valid():
#         client = Client()
#         client.register(
#             serializer.validated_data['username'],
#             serializer.validated_data['email'],
#             request.data['password'],
#             serializer.validated_data['phone_number']
#         )
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def Clientlogin(request):
#     try:
#         client = Client.objects.get(username=request.data['username'])
#         if client.login(request.data['username'], request.data['password']):
#             serializer = ClientSerializer(client)
#             return Response(serializer.data)
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
#     except Client.DoesNotExist:
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def Clientreset_password(request):
#     new_password = Client().reset_password(request.data['username'])
#     if new_password:
#         return Response({'new_password': new_password})
#     else:
#         return Response({'error': 'Invalid username'}, status=status.HTTP_400_BAD_REQUES)


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client
from .serializers import (
    LoginSerializer,
    PasswordResetSerializer,
    RegisterSerializer,
)


class RegisterClientView(generics.CreateAPIView):
    queryset = Client.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginClientView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if user:
            login(request, user)
            return Response({"detail": "Successfully logged in."})
        else:
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LogoutClientView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Successfully logged out."})


class PasswordResetClientView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        user = Client.objects.filter(email=email).first()
        if user:
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            # Send email with uidb64 and token here
            return Response({"detail": "Password reset email sent."})
        else:
            return Response(
                {"detail": "User with this email does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )










from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Produit
from .serializers import ProductSerializer

def ajouter_au_panier(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    panier = request.session.get('panier', {})
    quantite = panier.get(str(produit_id), 0)
    panier[str(produit_id)] = quantite + 1
    request.session['panier'] = panier
    return JsonResponse({"success":True}, safe=False)

def supprimer_du_panier(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    panier = request.session.get('panier', {})
    if str(produit_id) in panier:
        del panier[str(produit_id)]
        request.session['panier'] = panier
    return JsonResponse({"success":True}, safe=False)


def afficher_panier(request):
    panier = request.session.get('panier', {})
    produits = []
    total = 0
    for produit_id, quantite in panier.items():
        produit = get_object_or_404(Produit, pk=produit_id)
        produits.append({
            'titre': produit.titre,
            'prix': produit.prix,
            'quantite': quantite,
            'total': quantite * produit.prix
        })
        total += quantite * produit.prix
    return JsonResponse({'produits': produits, 'total': total}, safe=False)





from .serializers import ProductSerializer

class ProductSearch(APIView):
    def get(self, request, query):
        products = Produit.objects.filter(titre__icontains=query)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)