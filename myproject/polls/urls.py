from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    # path("<int:question_id>/", views.detail, name='detail'),
    # 함수형에서는 question_id 를 인자로 넘겨주지만 클래스에서는 넘기지 않기 때문에 pk 로 받아서 찾아야 한다.
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    path("<int:question_id>/vote/", views.vote, name='vote'),
    # path("<int:question_id>/results/", views.results, name='results'),
    path("<int:pk>/results/", views.ResultView.as_view(), name='results'),
]