from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render

@staff_member_required
def top_purchaser(request):
    users = User.objects.annotate(
        purchase_count = Coalesce(Sum("order__item__quantity"), 0)
    )
    maximum = users.order_by("-purchase_count").first()

    leaders = []
    if maximum and maximum.purchase_count > 0:
        leaders = users.filter(
            purchase_count = maximum.purchase_count
        ).order_by("username", "id")

    return render(request, "movies/reports/top_purchaser.html", {
        "template_data": { "title": "Top Purchaser", "leaders": leaders,
        },
    })

    
        
        
        
        
        
        
        
