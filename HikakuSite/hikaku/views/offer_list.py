from django.views import generic
from ..models import ProductModel, OfferModel, BookMarkModel
from django.shortcuts import redirect, render

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
        return self.render_to_response({"items": offer_objects})