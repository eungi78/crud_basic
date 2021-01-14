from django import forms
from .models import Post

class PostForm(forms.ModelForm): 
    # Model에 맞는 폼을 만들어주고 유효성까지 검사해주는 것
    class Meta: # 클래스 안에 있는 meta class는 자기 외부 클래스를 설명해주는 역할
        model = Post # 어떤 모델을 대상으로 모델을 만들 것이냐.
        fields = '__all__' # 어떤 필드? ['writer', 'title']처럼 작성하면 이 두 가지만 하면 두 가지만 입력하게 만듦.