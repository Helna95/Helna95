from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()

#router.register(r'Contacts', views.ContactList)
#router.register(r'Users', views.UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/Contacts/', views.ContactList.as_view()),
    path(r'api/Contacts/Update/<int:pk>', views.ContactList.as_view()),
    path(r'api/Contacts/Add/', views.ContactList.as_view()),
    path(r'api/Contacts/Delete/<int:pk>', views.ContactList.as_view()),
    path(r'api/Users/', views.UsersList.as_view()),
]
