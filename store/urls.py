from django.urls import path
from django.urls import path
from store import views
from .views import *
from .views import Cart
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetpasswordForm
urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name="home"),
    # path('product-detail', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.cart, name='cart'),
    #path('cart/', views.CartView.as_view(), name='cart'),
    path('showcart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart, name = 'pluscart'),
    path('minuscart/', views.minus_cart, name = 'minuscart'),
    path('removecart/', views.remove_cart, name= 'removecart'),
    path('checkout/', views.checkout, name='checkout'),
    path('address/', views.address, name='address'),
    path('order/', views.orders, name='order'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('agreculture/', views.agreculture, name='agreculture'),
    path('agreculture/<slug:data>', views.agreculture, name='agreculturedata'),
    path('tools/', views.tool, name='tools'),
    path('tools/', views.tool, name='tools'),
    path('wepons/', views.wepon, name='wepons'),


    path('accounts/login/', auth_views.LoginView.as_view(template_name='store/login.html', authentication_form=LoginForm), name='login'),
    # path('profile/', views.profile, name='profile'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='store/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='store/passwordchange_done.html'), name='passwordchangedone'),
    
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='store/passwordreset.html', form_class=MyPasswordResetForm), name="passwordreset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='store/passwordreset_done.html'), name="passwordreset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='store/passwordreset_confirm.html', form_class=MySetpasswordForm), name="passwordreset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='store/passwordreset_complete.html'), name="passwordreset_complete"),

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
