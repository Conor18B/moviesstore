from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def top_commenter(request):
    users = User.objects.annotate(comment_count=Count("review"))
    maximum_user = users.order_by('-comment_count').first()
    leaders =[]
    if maximum_user and maximum_user.comment_count > 0:
        leaders = users.filter(comment_count=maximum_user.comment_count).order_by("username")

    return render(request, "movies/reports/top_commenter.html", 
                  {"template_data": {
                      "title": "Top Commenter",
                      "leaders": leaders,
                  }})
