from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'lab_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'lab_1.view.index', name='index'),
    url(r'^search/', 'lab_1.view.search', name='search'),
    url(r'^add/', 'lab_1.view.add', name='add'),
    url(r'^home/', 'lab_1.view.home', name='home'),
    #url(r'/', 'lab_1.view.home', name='home'),
    url(r'^delete/', 'lab_1.view.delete', name='delete'),

]
