"""python_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from rest_framework import routers
from rest_framework_nested import routers



from django.conf.urls import url
from django.contrib import admin
from my_app import views
# from views import SchoolViewSet, StudentViewSet


# router = routers.DefaultRouter()
router = routers.SimpleRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

router.register(r'schools', views.SchoolViewSet)
router.register(r'students', views.StudentViewSet)

# do nested url
school_router = routers.NestedSimpleRouter(router, r'schools', lookup='schools')
school_router.register(r'students', views.StudentViewSet, base_name='students')

# student_router = routers.NestedSimpleRouter(router, r'students', lookup='student')
# student_router.register(r'students', views.StudentViewSet, base_name='students')


# router.register(r'schools', views.SchoolViewSet, base_name=)
# domains_router = routers.NestedSimpleRouter(router, r'domains', lookup='domain')


urlpatterns = [
	url(r'^', include(router.urls)),
	# url(r'^api/', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	#    url(r'^admin/', admin.site.urls),
    url(r'^', include(school_router.urls)),
   ]
# urlpatterns += router.urls

