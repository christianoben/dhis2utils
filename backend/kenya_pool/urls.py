from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/locations/', include('locations.urls')),
    path('api/pools/', include('pools.urls')),
    path('api/games/', include('games.urls')),
    path('api/leaderboards/', include('leaderboards.urls')),
    path('api/recommendations/', include('recommendations.urls')),
    path('api/notifications/', include('notifications.urls')),
]
