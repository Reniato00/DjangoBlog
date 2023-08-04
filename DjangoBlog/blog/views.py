from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from blog.models import Service,FormRequest
def index(request):
    services = Service.objects.all().order_by('-id')[:3]
    return render(request, 'index.html',{
        "services": services
    })

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html',{
        "services" : services
    })

def contact(request):
    return render(request, 'contact.html')

def save_create(request):
    servicio = Service(
        title = "test3",
        content = "test3",
        public = True,
        attachment_pdf = "",
        image = ""
    )
    servicio.save()
    return HttpResponse("Servicio creado")

def dashboardservices(request):
    services = Service.objects.all().order_by('-id')[:2]
    return render(request, 'dashboardservices.html',{
        "services" : services
    })

def save_form(request):
    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        form_request = FormRequest(
            name = name,
            email = email
        )
        form_request.save()
        return redirect('index')
    return render(request, 'dashboardcontact.html')