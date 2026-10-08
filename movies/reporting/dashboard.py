from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

@staff_member_required
def dashboard(request):
    return render(request, "movies/reports/dashboard.html", {
        "template_data": {"title": "Admin Reports"}})