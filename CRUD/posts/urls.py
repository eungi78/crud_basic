from django.urls import path
from . import views

app_name = 'posts'  # 이걸 명시해줘야 create에서 name 사용가능

urlpatterns = [
    path('', view=views.post_list, name="list"),
    # int로 받아온 값을 post_id로 넘기겠다.
    path('<int:post_id>', view=views.post_detail, name='detail'),
    path('create/', view=views.create_post, name='create'),
]
