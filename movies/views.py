from django.shortcuts import render,redirect
from .models import Movie,Watched
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login')
def index(request):
        if request.method == 'POST':
                id = request.POST.get('id')
                rate = request.POST.get('rate')
                if rate:
                        m = Movie.objects.get(id = id)
                        w = Watched(user = request.user, movie = m, rating = rate)
                        w.save()
                return redirect('movies:index')
        else:
                not_watched = Movie.objects.exclude(id__in = Watched.objects.filter(user = request.user.id).select_related().values('movie')).order_by('year','movie')
                context = {'not_watched':not_watched}                        
                return render(request, 'movies/index.html', context)

@login_required
def watched(request):
        if request.method == 'GET':
                watched = Watched.objects.filter(user = request.user.id).select_related().values('id','movie__movie','rating','movie__tamil','movie__year')
                context = {'watched':watched}
                return render(request, 'movies/watched.html', context)
        else:
                id = request.POST.get('id')
                if 'delete' in request.POST:
                        ob = Watched.objects.get(id = id)
                        ob.delete()
                else:
                        rate = request.POST.get('rate')
                        if rate:
                                ob = Watched.objects.get(id = id)
                                ob.rating = rate
                                ob.save()
                return redirect('movies:watched') 