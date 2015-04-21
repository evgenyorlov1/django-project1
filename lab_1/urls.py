from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'lab_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'lab_1.view.index'),
    url(r'^input/', 'lab_1.view.search'),
    url(r'^add/', 'lab_1.view.add'),
    url(r'^home/', 'lab_1.view.home'),

]
