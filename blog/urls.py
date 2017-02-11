from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

url(r'^base/$', views.base, name='base'),

url(r'^gallery/$', views.gallery, name='gallery'),

url(r'^contact/$', views.contact, name='contact'),

url(r'^services/$', views.services, name='services'),

url(r'^Deptresource/$', views.deptresource, name='deptresource'),


url(r'^dept/$', views.dept, name='dept'),

url(r'^Nondept/$', views.nondept, name='nondept'),

url(r'^reg/$', views.reg, name='reg'),

url(r'^Blogs/$', views.blogs, name='blogs'),

url(r'^news/$', views.post_list2, name='news'),

url(r'^nondeptresource/$', views.nondeptresource, name='nondeptresource'),

url(r'^contacts/$', views.contacts, name='contacts'),


url(r'^post/slist/$', views.studentlist, name='studentlist'),
url(r'^blog/reg/$', views.regshow, name='regshow'),
url(r'^rspshow$', views.rspshow, name='rspshow'),



]
