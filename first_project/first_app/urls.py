from django.urls import include, path

from . import views 

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<num>', views.show),
    path('<num>/edit', views.edit),
    path('<num>/delete', views.destroy),
    path('delete/<user_id>', views.delete_user)
]