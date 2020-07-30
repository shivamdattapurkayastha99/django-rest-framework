"""restproject URL Configuration

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
from api_basic.views import article_list
from api_basic.views import article_detail,ArticleAPIView,ArticleDetails,GenericAPIView,ArticleViewSet,ArticleGenericViewSet,ModelArticleViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
# router.register('article',ArticleViewSet,basename='article')
# router.register('article',ArticleGenericViewSet,basename='article')
router.register('article',ModelArticleViewSet,basename='article')
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('api_basic.urls')),
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
    # path('viewset/', include(router.urls)),
    # path('viewset/<int:pk>/', include(router.urls)),
    # path('viewset/', include(router.urls)),
    # path('viewset/<int:pk>/', include(router.urls)),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    


]
