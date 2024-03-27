from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    headers = Header.objects.first()
    accueil = Accueil.objects.first()
    presentations = Presentation.objects.all()
    valeurs = Valeur.objects.all()
    carasteristique1s = Carasteristique1.objects.all()
    carasteristique2 = Carasteristique2.objects.first()
    carasteristique3s = Carasteristique3.objects.all()
    questions = Question.objects.all()
    temoins = Temoin.objects.all()
    socials = Social.objects.all()
    footers = Footer.objects.first()
    liens = Lien.objects.all()
    offres = Offre.objects.all()
    infos = Info.objects.first()
    section = Section.objects.first()

    context={
        'headers': headers,
        'accueil': accueil,
        'presentations':presentations,
        'valeurs':valeurs,
        'carasteristique1s':carasteristique1s,
        'carasteristique2':carasteristique2,
        'carasteristique3s':carasteristique3s,
        'questions':questions,
        'temoins':temoins,
        'socials':socials,
        'footers':footers,
        'liens':liens,
        'offres':offres,
        'infos':infos,
        'section':section,
        
    }
    return render(request, 'home.html',context)

def about(request):
    headers = Header.objects.first()
    abouts = About.objects.first()
    domaines = Domaine.objects.all()
    partenaires = Partenaire.objects.all()
    blogs = Blog.objects.all()
    socials = Social.objects.all()
    footers = Footer.objects.first()
    liens = Lien.objects.all()
    offres = Offre.objects.all()
    infos = Info.objects.first()

    context={
        'headers': headers,
        'abouts':abouts,
        'domaines':domaines,
        'partenaires':partenaires,
        'blogs':blogs,
        'socials':socials,
        'footers':footers,
        'liens':liens,
        'offres':offres,
        'infos':infos,
    }
    
    return render(request, 'about.html',context)

def service(request):
    headers = Header.objects.first()
    services = Service.objects.first()
    offres = Offre.objects.all()
    postes = Poste.objects.all()
    projets = Projet.objects.all()
    socials = Social.objects.all()
    footers = Footer.objects.first()
    liens = Lien.objects.all()
    infos = Info.objects.first()
    section = Section.objects.first()

    context={
        'headers': headers,
        'services': services,
        'offres':offres,
        'postes':postes,
        'projets':projets,
        'socials':socials,
        'footers':footers,
        'liens':liens,
        'infos':infos,
        'section':section,
        
    }
    return render(request, 'service.html',context)

def team(request):
    headers = Header.objects.first()
    teams = Team.objects.first()
    postes = PosteMembre.objects.all()
    m1 = Methode1.objects.first()
    m2 = Methode2.objects.first()
    m3 = Methode3.objects.first()
    cadres = Cadre.objects.all()
    partenaires = Partenaire.objects.all()
    socials = Social.objects.all()
    footers = Footer.objects.first()
    liens = Lien.objects.all()
    offres = Offre.objects.all()
    infos = Info.objects.first()
    section = Section.objects.first()

    context={
        'headers': headers,
        'teams': teams,
        'postes':postes,
        'm1':m1,
        'm2':m2,
        'm3':m3,
        'cadres': cadres,
        'partenaires': partenaires,
        'socials':socials,
        'footers':footers,
        'liens':liens,
        'offres':offres,
        'infos':infos,
        'section':section,
        
    }
    return render(request, 'team.html',context)

def contact(request):
    headers = Header.objects.first()
    contacts= Contact.objects.first()
    cards = Card.objects.all()
    socials = Social.objects.all()
    footers = Footer.objects.first()
    liens = Lien.objects.all()
    offres = Offre.objects.all()
    infos = Info.objects.first()

    context={
        'headers': headers,
        'contacts':contacts,
        'cards':cards,
        'socials':socials,
        'footers':footers,
        'liens':liens,
        'offres':offres,
        'infos':infos,
        
    }
    return render(request, 'contact.html',context)

def blog(request):
    return render(request, 'blog.html')

