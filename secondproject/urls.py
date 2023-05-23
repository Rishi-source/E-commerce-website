"""secondproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from secondapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("about/",views.aboutpage,name="about"),
    path("contact/",views.contactpage,name="contact"),
    path("signup/",views.register,name="reg"),
    path("check_user/",views.check_user,name="check_user"),
    path("user_login",views.user_login,name="user_login"),
    path("cust_dashboard/",views.cust_dashboard,name="cust_dashboard"),
    path("seller_dashboard/",views.seller_dashboard,name="seller_dashboard"),
    path("user_logout/",views.user_logout,name="user_logout"),
    path("edit_profile/",views.edit_profile,name="edit_profile"),
    path("change_password/",views.change_password,name="change_password"),
    path("add_product/",views.add_product_view,name="add_product_view"),
    path("my_products/",views.my_products,name="my_products"),

    path("single_product",views.single_product, name="single_product"),
    path("update_product",views.update_product, name="update_product"),
    path("delete_product",views.delete_product, name="delete_product"),
    path("all_products",views.all_products, name="all_products"),
    path("sendemail",views.sendemail, name="sendemail"),
    path("forgotpass",views.forgotpass, name="forgotpass"),
    path("reset_password",views.reset_password,name="reset_password"),
    path("cart",views.add_to_cart,name="cart"),
    path("get_cart_data",views.get_cart_data,name="get_cart_data"),
    path("change_quan",views.change_quan,name="change_quan"),
    path('payment_success',views.payment_success,name="payment_success"),
    path('payment_failed',views.payment_failed,name="payment_failed"),
    path('order_history',views.order_history,name="order_history"),
    path('wallet',views.wallet,name = "wallet"),
    path('buy_now',views.buy_now,name="buy_now"),
    path('wishlist',views.wish,name="wishlist"),
    path('seller_profile',views.seller_profile,name="seller_profile"),
    path('OrderDetail',views.OrderDetails,name="OrderDetail"),
    path('Review',views.review,name="Review"),
    path('table',views.review_table,name="table"),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
