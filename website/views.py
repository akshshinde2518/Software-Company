from django.shortcuts import render

from website import models

# Create your views here.
def home(req):
    features = models.Feature.objects.all()
    about = models.About.objects.all()
    counters = models.Counter.objects.all()
    services = models.Service.objects.all()
    sliders = models.Slider.objects.all()
    challenge = models.Challenge.objects.all()
    projects = models.Project.objects.all()
    wcu = models.WhyChooseUs.objects.all()
    testimonials = models.Testimonial.objects.all()
    blog = models.Blog.objects.all()
    partners = models.Partner.objects.all()
    obj = {"features":features,"about":about,"counters":counters,"services":services,"sliders":sliders,"challenge":challenge,
           "projects":projects,"wcu":wcu,"testimonials":testimonials,"blog":blog,"partners":partners}
    return render(req,"home.html",obj)

def about (req):
    counter = models.Counter.objects.all()
    part = models.Partner.objects.all()
    wcu = models.WhyChooseUs.objects.all()
    testimonials = models.Testimonial.objects.all()
    members = models.Member.objects.all()

    obj = {"counter":counter,"part":part,"wcu":wcu,"testimonials":testimonials,"members":members}
    return render(req,"about.html",obj)

def services (req):
    services = models.Service.objects.all()
    partners = models.Partner.objects.all()

    obj = {"services":services,"partners":partners}
    return render(req,"services.html",obj)

def blog (req):
    blog = models.Blog.objects.all()
    obj = {"blog":blog}
    return render(req,"blog.html",obj)

def contactus (req):
    return render(req,"contactus.html")