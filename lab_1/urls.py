from django.conf.urls import include, url
from django.contrib import admin
import view

urlpatterns = [
    # Examples:
    # url(r'^$', 'lab_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'lab_1.view.view1'),
    url(r'^input/', 'lab_1.view.form'),
]
