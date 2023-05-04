from django.urls import path
from . import views 
from knox import views as knox_views
# from django.urls import path
from .views import RegisterView, LoginView, PasswordResetView, LogoutView,RestaurateurList,DeleteRestaurateurView, ProductSearch,RegisterClientView,LoginClientView,LogoutClientView,PasswordResetClientView
# ,Clientregister,Clientlogin,Clientreset_password
urlpatterns = [
    path('',views.ListRestaurantView.as_view(), name='resto'),
    path('add_resto/',views.CreateRestaurantView.as_view(), name='create_resto'),
    path('<pk>/update_resto/',views.UpdateRestaurantView.as_view(), name='resto_update'),
    path('<pk>/delete_resto/',views.DeleteRestaurantView.as_view(), name='resto_delete'),
    path('commentaire/',views.ListCommentaireView.as_view(), name='commentaire'),
    path('add_commentaire/',views.CreateCommentaireView.as_view(), name='create_commentaire'),
    path('produit/',views.ListProduitView.as_view(), name='produit'),
    path('add_produit/',views.CreateProduitView.as_view(), name='create_produit'),
    path('<pk>/update_produit/',views.UpdateProduitView.as_view(), name='produit_update'),
    path('<pk>/delete_produit/',views.DeleteProduitView.as_view(), name='produit_delete'),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view(), name="login"),
    path('password_reset/', PasswordResetView.as_view()),
    path('LogoutView/', LogoutView.as_view()),
    path('restaurateurs/', RestaurateurList.as_view(), name='restaurateur-list'),
    path('restaurateur/<int:pk>/delete/', DeleteRestaurateurView.as_view(), name='delete_restaurateur'),
    path('registerclient/',RegisterClientView.as_view(), name='registerclient'),
    path('loginclient/', LoginClientView.as_view(), name='loginclient'),
    path('deconect/', LogoutClientView.as_view(), name='deconect'),
    path('resetclient/', PasswordResetClientView.as_view(), name='resetclient'),
    path('panier/ajouter/<int:produit_id>/', views.ajouter_au_panier),
    path('panier/supprimer/<int:produit_id>/', views.supprimer_du_panier),
    path('cart/', views.afficher_panier),
    path('api/search/<str:query>/', ProductSearch.as_view(), name='search')
    # path('confirmresetclient/', ClientPasswordResetConfirmView.as_view(), name='confirmresetclient'),


    

]
