from django.urls import path
from news import views
urlpatterns = [
    path("<category_id>/", views.CategoryNameView.as_view(), name="category_news")
]
