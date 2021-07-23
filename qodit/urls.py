"""qodit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('api/navbar/', include('Navbar.urls')),
    path('api/herobox/',include('HeroBox.urls')),
    path('api/features/',include('Features.urls')),
    path('api/services/',include('Services.urls')),
    path('api/aboutus/',include('AboutUs.urls')),
    path('api/testimonials/',include('Testimonial.urls')),
    path('api/team/',include('Team.urls')),
    path('api/contactus/',include('ContactUs.urls')),
    path('api/chooseusleft/',include('ChooseUsleft.urls')),
    path('api/chooseusright/',include('ChooseUsRight.urls')),



    # path(r'^keycloak/', include('django_keycloak.urls')),
    path('admin/', admin.site.urls),

]
