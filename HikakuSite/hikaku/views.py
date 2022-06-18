import imp
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm
from functools import reduce
from django.db.models import Q
from .models import ProductModel, OfferModel, BookMarkModel
from .tables import ProductTable
from django.shortcuts import redirect, render

class MyPage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'hikaku/mypage.html'
    
    def get(self, request, **kwargs):
        bookmark_query = BookMarkModel.objects
        
        # user_idでフィルタ
        user_id = self.request.user.id
        if user_id == None or user_id == "":
            # 検索条件が未指定の場合は全件表示
            bookmark_objects = None
        else:
            bookmark_objects = bookmark_query.filter(user_id=user_id).all()
            
        bookmark_products = []
        for object in bookmark_objects:
            print(type(object.product))
            bookmark_products.append(object.product.name)
            
        context = {
            'username': self.request.user.username,
            'items': bookmark_objects
        }
        return self.render_to_response(context)
    
    def post(self, request, **kwargs):
        user_id = self.request.user.id
        product_id = request.POST["product_id"]
        
        BookMarkModel.objects.filter(user_id=user_id, product_id=product_id).delete()
        
        url = request.get_full_path()
        
        return redirect(url)

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'hikaku/login.html'


class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'hikaku/logout.html'
    

class Search(generic.TemplateView):
    template_name = 'hikaku/search.html'

class SearchResult(generic.TemplateView):
    template_name = 'hikaku/search_result.html'
    
    def get(self, request, *args, **kwargs):
        product_query = ProductModel.objects.order_by("name")
        # nameでフィルタ
        name = request.GET.get("q")
        if name == None or name == "":
            # 検索条件が未指定の場合は全件表示
            product_objects = product_query.all()
        else:
            product_objects = product_query.filter(name__contains=name).all()
        
        bookmark_query = BookMarkModel.objects
        # user_idでフィルタ
        user_id = self.request.user.id
        if user_id == None or user_id == "":
            # 検索条件が未指定の場合は全件表示
            bookmark_objects = None
        else:
            bookmark_objects = bookmark_query.filter(user_id=user_id).all()
        
        bookmark_id_list = []
        
        if bookmark_objects:
            for object in bookmark_objects:
                bookmark_id_list.append(object.product.id)
        
        # HTMLに出力する内容をセット
        context = {"items": product_objects, 
                   "bookmark_id_list": bookmark_id_list,
                   "record_count": product_objects.count()} # レコード件数
        
        # HTMLを出力
        return render(request, self.template_name, context)
        
    def post(self, request, **kwargs):
        user_id = self.request.user.id
        product_id = request.POST["product_id"]
        
        model = BookMarkModel(user_id=user_id, product_id=product_id)
        model.save()
        
        url = request.get_full_path()
        
        return redirect(url)

class OfferList(generic.TemplateView):
    template_name = 'hikaku/offer_list.html'
    
    def get(self, request, *args, **kwargs):
        offer_query = OfferModel.objects.order_by("price")
        
        # product_idでフィルタ
        product_id = request.GET.get("q")

        if product_id == None or product_id == "":
            offer_objects = None
        else:
            offer_objects = offer_query.filter(product_id=product_id).all()

        # HTMLに出力する内容をセット
        context = {"items": offer_objects}
        
        # HTMLを出力
        return render(request, self.template_name, context)