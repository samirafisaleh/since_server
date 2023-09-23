
from rest_framework import routers

from app.views import EntryViewSet

router = routers.DefaultRouter()
router.register(r'entry', EntryViewSet)





