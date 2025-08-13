from django.urls import path ,include
from .router import router
from .views import Bookgenricsupdate , Bookgenrics
urlpatterns = [
    path('all_books' ,Bookgenrics.as_view() ,name='all_book'),
    path('all_books/<int:pk>' ,Bookgenricsupdate.as_view() ,name='book'),
    path('', include(router.urls))
]



