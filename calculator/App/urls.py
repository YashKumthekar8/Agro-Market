from django.urls import path,include
from App import views
urlpatterns = [
 
    path('ohms-law-calculator/',views.ohmslawcalculator),
    path('compton-wavelength-calculator/',views.comptonwavelengthcalculator),
    path('acceleration-of-particle-in-electric-field-calculator/',views.accelerationofparticleinelectricfield),
    path('voltage-divider-calculator/',views.voltagedividercalculator),
    path('weight-other-planets/',views.weightotherplanets),
    path('arrow-speed-calculator/',views.arrowspeedcalculator),
    path('wet-bulb-calculator/',views.wetbulbcalculator),
    path('momentum-with-velocity-calculator/',views.momentumwithvelocitycalculator),
    path('momentum-with-time-calculator/',views.momentumwithtimecalculator),
    path('friction-loss-calculator/',views.frictionlosscalculator),
    path('specific-heat-calculator/',views.specificheatcalculator),
    path('half-life-calculator/',views.halflifecalculator),


]