from django.conf.urls import url
from . import views
from django.urls import path

app_name='game_results'
urlpatterns=[
    path('',views.index,name='index'),
    path('games/',views.games,name='games'),
    path('games/<int:game_id>/',views.game,name='game'),
    path('new_game/',views.new_game,name='new_game'),
    path('new_result/<int:game_id>/',views.new_result,name='new_result'),
    path('edit_result/<int:result_id>/',views.edit_result,name='edit_result'),
]