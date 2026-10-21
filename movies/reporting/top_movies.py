from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from movies.models import Movie

@staff_member_required
def top_movies(request):
    purchased = Movie.objects.annotate(purchase_count=Coalesce(Sum("item__quantity"), 0))
    reviewed = Movie.objects.annotate(review_count = Count("review"))

    purchase_maximum = purchased.order_by("-purchase_count").first()
    review_maximum = reviewed.order_by("-review_count").first()

    purchase_leaders = []
    review_leaders = []

    if purchase_maximum and purchase_maximum.purchase_count > 0:
        purchase_leaders = purchased.filter(purchase_count=purchase_maximum.purchase_count).order_by("name", "id")

    if review_maximum and review_maximum.review_count > 0:
        review_leaders = reviewed.filter(review_count=review_maximum.review_count).order_by("name", "id")

    return render(
        request, "movies/reports/top_movies.html", {
            "template_data" : {
                "title" : "Most Purchased and Reviewed Movies",
                "purchase_leaders" : purchase_leaders,
                "review_leaders" : review_leaders,
            },
        },
    )
