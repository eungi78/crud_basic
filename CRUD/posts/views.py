from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.


def post_list(request):
    '''
    Retrieve, Read == SELECT
    저장된 모든 포스트를 렌더링하는 뷰
    '''
    posts = Post.objects.all()  # 정확히는 여기가 Retrieve(Read)
    ctx = {'posts': posts}

    return render(request, template_name='posts/list.html', context=ctx)


def post_detail(request, post_id):  # post_id 는 url로부터 받아온 것
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


def create_post(request):
    '''
    Create(C)
    포스트를 새로 생성한다
    request method ==> GET(url 입력), POST(저장하기), PUT, DELETE... 생활코딩
    '''
    if request.method == 'POST':
        # 글쓰기 칸을 저장하기 눌렀을 때
        form = PostForm(request.POST)  # POST METHOD로 작성한 것을 REQUEST 객체로 받아옴
        if form.is_valid():  # 입력한 것이 형식과 맞는지 확인
            # python 은 interpreter 언어이기때문에 밑에서 오류가 발생했더라도 db에 반영이 됨.
            form.save()
            # redirct는 url 중 한 군데를 골라서 다시 그곳으로 돌아갈게
            return redirect('posts:list')  # posts app 에서 list이란 name을 찾자

    else:
        # 글쓰기 칸을 보여줄 때, 즉 get방식으로 접근했을 때
        form = PostForm()  # 인스턴스 생성
        ctx = {'form': form}
        return render(request, template_name='posts/post_form.html', context=ctx)
