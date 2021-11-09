from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import tree
from django.views.generic.base import ContextMixin, TemplateView
from django.views.generic.detail import BaseDetailView, SingleObjectTemplateResponseMixin

class JsonResponseMixin:
    model = None
    context = {}
    """
    A mixin that can be used to render JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(self.get_data(), json_dumps_params={'indent': 2}, **response_kwargs)

    def get_data(self):
        """
        HARDCODED!!!  
        Returns an object that will be serialized as JSON by json.dumps().
        """
        if self.model:
            query = self.model.objects.all()
            querylist = []
            for item in query:
                querylist.append({
                    f'{item.name}': {
                        'author':f'{None  if not self.get_object_does_not_exist(item.author_set) else item.author_set.get().name}',
                        'date_added':item.pub_date.date().isoformat()
                    }
                }
            )
            self.context.update(
                books = querylist
            )
        return self.context

    def get_object_does_not_exist(self, obj):
        try:
            obj.get()
            return True
        except ObjectDoesNotExist:
            return False

class JsonTemplateView(JsonResponseMixin, TemplateView):
    """
    This view can then be deployed in the same way as any other TemplateView, with exactly the same behavior – 
    except for the format of the response. Adapted from Django documentation.
    """
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

class JsonDetailView(JsonResponseMixin, BaseDetailView):
    """
    This view can then be deployed in the same way as any other DetailView, with exactly the same behavior – 
    except for the format of the response. Adapted from Django documentation.
    """
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

class HybridJsonDetailView(JsonResponseMixin, SingleObjectTemplateResponseMixin, BaseDetailView):
    """
    
    """
    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get('format') == 'json':
            return self.render_to_json_response(context, **response_kwargs)
        else:
            return super().render_to_json_response(context, **response_kwargs)