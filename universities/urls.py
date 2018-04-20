from django.conf.urls import patterns, include, url
from rest_framework import routers

from universities.views import UniversitiesViewSet, AwardsDetailsViewSet

router = routers.DefaultRouter()
router.register(r'universities', UniversitiesViewSet)
router.register(r'awardsdetails', AwardsDetailsViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sourcing_tool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),

    
)
