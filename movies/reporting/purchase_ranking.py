from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required



@staff_member_required
def purchase_ranking(request):
    users = User.objects.annotate(purchase_count = Coalesce(Sum('order__item__quantity'), 0)).order_by('-purchase_count', 'username', 'id')

    raw_limit = request.GET.get("limit", "").strip()

    error = ""

    if raw_limit:
        try:
            limit = int(raw_limit)
            if limit < 1:
                raise ValueError
        except ValueError:
            error = "Enter a positive whole number or nothing"
        else:
            users = users[:limit]

    return render(request, "movies/reports/purchase_ranking.html", 
                  {"template_data": {
                      "title": "Purchase Ranking",
                      "users": users,
                      "limit": raw_limit,
                      "error": error, 
                  }})



