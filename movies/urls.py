from django.urls import path
from . import views
from .reporting.dashboard import dashboard
from .reporting.top_purchaser import top_purchaser
from .reporting.purchase_ranking import purchase_ranking
from .reporting.top_commenter import top_commenter
from .reporting.top_movies import top_movies

urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),
    path('<int:id>/review/create/', views.create_review, 
         name='movies.create_review'),
    path('<int:id>/review/<int:review_id>/edit/',
        views.edit_review, name='movies.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/',
        views.delete_review, name='movies.delete_review'),
    path('<int:id>/review/<int:review_id>/report/',
        views.report_review, name='movies.report_review'),
    path("reports/", dashboard, name="movies.reports"),
    path("reports/purchase-ranking/", purchase_ranking,
         name="movies.purchase_ranking"),
    path(
        "reports/top-purchaser/",
        top_purchaser,
        name="movies.top_purchaser",
    ),
    path(
        "reports/top-commenter/",
        top_commenter,
        name="movies.top_commenter",
    ),
    path("reports/top-movies/", top_movies, name="movies.top_movies"),
]
