from django.contrib import admin
from django.urls import path, include

from eventex.core.views import home, speaker_detail, talk_list

urlpatterns = [
    path('', home, name='home'),
    path('subscriptions/', include('eventex.subscriptions.urls')),
    path('talks/', talk_list, name='talk_list'),
    path('speakers/<slug:slug>/', speaker_detail, name='speaker_detail'),
    path('admin/', admin.site.urls),
]
