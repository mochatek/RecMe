from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recommend
import numpy as np
from movies.models import Movie, Watched

# Create your views here.
@login_required
def index(request):
    update_rec(request.user)
    recommended = Recommend.objects.filter(user = request.user.id).select_related().values('movie__movie', 'strength', 'movie__year', 'movie__tamil').order_by('-strength')
    context={'recommended':recommended}
    return render(request, 'recommend/index.html', context)

def update_rec(user):
        Recommend.objects.filter(user = user.id).delete()
        watched = Movie.objects.filter(id__in = Watched.objects.filter(user = user.id).select_related().values('movie'))
        if watched:
                rate = Watched.objects.filter(user = user.id).values('rating')
                # Convert to value list of genres
                wm_vl = watched.values_list('action', 'adventure', 'anthology', 'biographical', 'campus',
                                        'children', 'comedy', 'crime', 'drama', 'family', 'fantasy', 'fiction',
                                        'heist', 'historical', 'horror', 'masala', 'music', 'mystery',
                                        'patriotism', 'period', 'political', 'psychological', 'revenge', 'road',
                                        'romantic', 'satire', 'social', 'sport', 'suspense', 'thriller',
                                        'malayalam','tamil')
                rt_vl=rate.values_list('rating')
                # Convert list to nd array
                movie_mat = np.array(list(wm_vl))
                # Convert to 1-D array
                rate_mat = np.array(list(rt_vl)).ravel()
                weight_mat = movie_mat * rate_mat[:, None]
                user_prof = weight_mat.sum(axis = 0)
                user_prof = np.array([round(float(i) / sum(user_prof), 2) for i in user_prof])

                not_watched = Movie.objects.exclude(id__in = Watched.objects.filter(user = user.id).select_related().values('movie'))
                nwm_id_vl = not_watched.values_list('id')
                nwm_vl = not_watched.values_list('action', 'adventure', 'anthology', 'biographical', 'campus',
                                        'children', 'comedy', 'crime', 'drama', 'family', 'fantasy', 'fiction',
                                        'heist', 'historical', 'horror', 'masala', 'music', 'mystery',
                                        'patriotism', 'period', 'political', 'psychological', 'revenge', 'road',
                                        'romantic', 'satire', 'social', 'sport', 'suspense', 'thriller',
                                        'malayalam','tamil')
                pred_movie_mat = np.array(list(nwm_vl))
                pred_movie_id_mat = np.array(list(nwm_id_vl)).ravel()
                pred_weight_mat = pred_movie_mat * user_prof[None, :]
                recommend_mat = pred_weight_mat.sum(axis = 1) * 10
                for i in range(len(recommend_mat)):
                        if 10 >= recommend_mat[i] >= 6.5:
                                m = Movie.objects.get(id = pred_movie_id_mat[i])
                                r = Recommend(user = user, movie = m, strength = round(recommend_mat[i], 2))
                                r.save()

    