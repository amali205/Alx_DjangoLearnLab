from rest_framework.routers import DefaultRouter
from .views import Bookviewset ,Authorviewset


router = DefaultRouter()

router.register('books' , Bookviewset , basename='books')
router.register('author' , Authorviewset , basename='author')
