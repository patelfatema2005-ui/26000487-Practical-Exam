from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import LostFoundReport

@login_required
def dashboard(request):
    reports = LostFoundReport.objects.all().order_by('-date_reported')
    total_lost = reports.filter(report_type='LOST').count()
    total_found = reports.filter(report_type='FOUND').count()
    open_cases = reports.filter(status='OPEN').count()

    context = {
        'reports': reports,
        'total_lost': total_lost,
        'total_found': total_found,
        'open_cases': open_cases,
    }
    return render(request, 'dashboard.pyhtml', context) 
