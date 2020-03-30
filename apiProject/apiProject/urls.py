from api import views
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'notes', views.NoteViewSet)

urlpatterns = [

    # Admin url
    url(r'^admin/', admin.site.urls),

    # Page url
    url(r'^$', views.HomePageView.as_view()),
    url(r'^users/', views.UsersPageView.as_view()),
    url(r'^notes/', views.NotesPageView.as_view()),

    # Api urls
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls))

]
