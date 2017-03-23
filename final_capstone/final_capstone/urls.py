from django.conf.urls import url, include
from rest_framework import routers
from restaurant_notes import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'restaurant_notes', views.RestaurantNoteViewSet)
router.register(r'customer', views.CustomerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^deleteNote/(?P<pk>\d+)', views.deleteNote, name='deleteNote'),
]