from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Platform_view (TemplateView):
    template_name = 'third_task/platform.html'

def games_view (request):
    games = {
        'first': "ВИТАМИНЫ",
        'second': "МИНЕРАЛЫ",
        'third': "ДОБАВКИ",
    }
    return render(request, 'third_task/games.html', context=games)

class Cart_view (TemplateView):
    template_name = 'third_task/cart.html'