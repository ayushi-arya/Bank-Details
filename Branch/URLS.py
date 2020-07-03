
 from django.conf.urls import url, include
 from django.contrib import admin
 from api.views import ImportView   

 urlpatterns = [
     url(r'^admin/', admin.site.urls),
     url(r'^import/', ImportView.as_view(), name='import'),
     url(r'^api/', include('api.urls'))
 ]
