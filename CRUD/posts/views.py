from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.


def post_list(request):
    '''
    Retrieve, Read == SELECT
    저장된 모든 포스트를 렌더링하는 뷰
    '''
    posts = Post.objects.all()  # 정확히는 여기가 Retrieve(Read)
    ctx = {'posts': posts}

    return render(request, template_name='posts/list.html', context=ctx)


def post_detail(request, post_id):
    '''
    Retrieve, Read == SELECT
    url 파라미터로 가져온 post_id(pk)에 해당하는 특정 포스트만을 렌더링하는 뷰
    '''
    # print(pk) # -> url에서 넘겨준 parameter

    post = Post.objects.get(id=post_id)  # 정확히는 여기가 Retrieve(Read)
    # post = get_object_or_404(Post, id=pk) # get과 같은 역할을 수행하지만, 해당하는 객체를 못찾으면 404에러를 띄운다
    # 안정성 측면에서 get_object_or_404를 사용하는것이 더 선호된다.

    # print(dir(post)) # -> post의 내부 변수들을 보여준다
    # print(post.id) # -> 해당 post의 id는 (당연히) pk와 같다.
    ctx = {'post': post}

    return render(request, template_name='posts/detail.html', context=ctx)
