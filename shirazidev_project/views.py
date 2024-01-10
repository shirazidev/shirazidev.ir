from django.shortcuts import render
from services_app.models import Service
from project_app.models import Project
from project_app.models import Navbar
from contactus_app.models import Contact
from visitor_counter.models import Visitor
from work.models import Work
from footerprofile.models import Person


def c404(request):
    return render(request, '404.html', status=404)


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Phone = request.POST.get('Phone')
        subject = request.POST.get('subject')
        text = request.POST.get('text')
        Contact.objects.create(name=name, email=email, Phone=Phone, subject=subject, text=text)
    visitor, created = Visitor.objects.get_or_create(id=1)
    if not created:
        visitor.count += 1
        visitor.save()

    visitors = visitor.count
    services = Service.objects.all()
    projects = Project.objects.all()
    navbar = Navbar.objects.all()
    work = Work.objects.all()
    person = Person.objects.get(pk=1)
    homephoto = Person.objects.get(pk=2)
    return render(request, 'index.html',
                  {'services': services, 'projects': projects, 'visitors': visitors, 'works': work, 'person': person, 'homephoto': homephoto, 'navbar': navbar})
