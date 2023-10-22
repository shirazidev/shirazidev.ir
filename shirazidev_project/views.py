from django.shortcuts import render
from services_app.models import Service
from project_app.models import Project
from contactus_app.models import Contact

def c404(request):
    return render(request, '404.html', status=404)

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        text = request.POST.get('text')
        Contact.objects.create(name=name, email=email, subject=subject, text=text)

    services = Service.objects.all()
    projects = Project.objects.all()

    return render(request, 'index.html', {'services': services, 'projects': projects})
