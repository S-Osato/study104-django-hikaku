from django.views import generic
from functools import reduce
from django.db.models import Q
from ..models import ProductModel, OfferModel, BookMarkModel
from django.shortcuts import redirect, render


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
        return self.render_to_response(context)
        
    def post(self, request, **kwargs):
        user_id = self.request.user.id
        product_id = request.POST["product_id"]
        
        model = BookMarkModel(user_id=user_id, product_id=product_id)
        model.save()
        
        url = request.get_full_path()
        
        return redirect(url)
