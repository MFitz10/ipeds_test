from django.conf.urls import patterns, include, url
import dashboard.views as views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sourcing_tool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.main),
)
