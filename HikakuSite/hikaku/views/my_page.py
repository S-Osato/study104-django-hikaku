from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from ..models import BookMarkModel
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