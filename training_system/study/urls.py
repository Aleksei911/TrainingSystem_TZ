from django.urls import path, include
from .views import MyLessonsViewSet, MyLessonsByProductViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('my-lessons', MyLessonsViewSet, 'my-lessons')


urlpatterns = [
    path('by-product/<int:product_id>/lessons/', MyLessonsByProductViewSet.as_view({'get': 'list'})),
    path('', include(router.urls))
]