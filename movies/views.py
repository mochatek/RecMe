from django.shortcuts import render,redirect
from .models import Movie,Watched
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login')
def index(request):
        if request.method == 'POST':
                id = request.POST.get('id')
                rate = request.POST.get('rate')
                m = Movie.objects.get(id = id)
                w = Watched(user = request.user, movie = m, rating = rate)
                w.save()
                return redirect('movies:index')
        else:
                not_watched = Movie.objects.exclude(id__in = Watched.objects.filter(user = request.user.id).select_related().values('movie'))
                context = {'not_watched':not_watched}                        
                return render(request, 'movies/index.html', context)

@login_required
def watched(request):
        watched = Watched.objects.filter(user = request.user.id).select_related()
        context = {'watched':watched}
        return render(request, 'movies/watched.html', context)