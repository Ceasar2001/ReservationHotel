from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='landing_page.html'), name='landing_page'),
    path('reservations/', include('reservations.urls')),
]