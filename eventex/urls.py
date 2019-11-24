from django.contrib import admin
from django.urls import path, include

from eventex.core.views import speaker_detail, talk_list, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('subscriptions/', include('eventex.subscriptions.urls')),
    path('talks/', talk_list, name='talk_list'),
    path('speakers/<slug:slug>/', speaker_detail, name='speaker_detail'),
    path('admin/', admin.site.urls),
]
