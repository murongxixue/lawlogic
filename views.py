from django.shortcuts import render
from django.views.generic import View

from django.http import HttpResponse,JsonResponse,HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
# Create your views here.
class homeView(View):
    def get(self, request):
        # return JsonResponse(dict(code=200, msg="hello", data="ok"))
        return render(request, "index.html")
        
    def post(self, request):
        keyword = request.POST.get("keyword", "")
        if keyword:
            keyword = "你搜索了："+keyword
        else:
            keyword = "不能为空"
        return render(request, "index.html", {"keyword":keyword})

def your_view_function(request):
    show_section = True  # 这里定义一个布尔类型的变量show_section
    context = {
        'show_section': show_section,
        # 其他需要传递给模板的变量
    }
    return render(request, 'your_template.html', context)
# views.py

import openai

# 设置你的API密钥
api_key = "key"
openai.api_key = api_key

def your_view_function(request):
    # 获取用户输入的问题
    user_input = request.GET.get('question', '')

    # 调用ChatGPT的API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        temperature=0.7,
        max_tokens=3000
    )

    # 获取API返回的回答
    answer = response['choices'][0]['text']

    # 将回答传递给模板，然后渲染页面
    context = {
        'question': user_input,
        'answer': answer,
    }
    return render(request, 'your_template.html', context)
