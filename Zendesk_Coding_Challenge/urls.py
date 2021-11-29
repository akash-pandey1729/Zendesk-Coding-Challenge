"""
Zendesk_Coding_Challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
#from django.contrib import admin
from django.urls import path, include

import ticket.views as ticket_views
import user.views as user_views

urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls),

    path('', user_views.login, name = 'user-login'),
    path('logout/', user_views.logout, name = 'user-logout'),

    path('home/<int:pk>', ticket_views.individual_ticket, name = 'individual-ticket'),

    path('home/', ticket_views.home, name = 'ticket-home'),
    path('about/', ticket_views.about, name = 'ticket-about'),
]