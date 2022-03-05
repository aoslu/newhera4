from django.urls import path
from newheraapp.views import anasayfa,about, contact, special, brand,briket, sosis, mese, nargile, robot

urlpatterns = [
    path('',anasayfa, name="anasayfa"),
    path('brand/', brand, name="brand"),
    path('about/', about, name="about"),
    path('special/', special, name="special"),
    path('contact/', contact, name="contact"),
    path('briket/', briket, name="briket"),
    path('sosis/', sosis, name="sosis"),
    path('mese/', mese, name="mese"),
    path('nargile/', nargile, name="nargile"),
    path('robot.txt/',robot, name="robot"),
]
