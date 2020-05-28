from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StatusSerializer
from .models import Status
from rest_framework import generics, mixins, permissions
from .forms import StatusForm 
import json
from rest_framework.authentication import SessionAuthentication



# Create your views here.
# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []

#     def get(self,request,format = None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs,many =True)
#         return Response(serializer.data)


#     def post(self,request, format = None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs,many =True)
#         return Response(serializer.data)


# CreateModelMixin --- POST method
# UpdateModelMixin --- PUT method
# DestroyModelMixin -- DELETE method

# class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView): #Create and List View
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer

#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs

#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)



'''Combination of Retrieve, Update an Destroy in a single view'''

# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'


'''
class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
'''

# '''This functions works same as lookup field'''
#     # def get_object(self, *args, **kwargs):
#     #     kwargs = self.kwargs
# '''abc / id j rakhda ni hunxa uta url ma ni same hunu paryo'''
#     #     kw_id = kwargs.get('abc') 
#     #     return Status.objects.get(id = kw_id)


# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer


# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer




 

# # class StatusCreateView(CreateView):
# #     queryset = Status.objects.all()
# #     form_class = StatusForm


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False

    return is_valid



"""One API end point for CRUDL"""

class StatusDetailAPIView(mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.RetrieveAPIView):

    permission_classes      = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes     = []
    serializer_class           = StatusSerializer
    queryset                   = Status.objects.all()
    lookup_field               = 'id'

    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class StatusAPIView(
                    mixins.CreateModelMixin,
                    generics.ListAPIView):
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes  = [SessionAuthentication] #Oauth, JWT
    serializer_class        = StatusSerializer
    passed_id = None 

    def get_queryset(self):
        request = self.request
        qs      = Status.objects.all()
        query   = request.GET.get('q')
        if query is not None:
            qs  = qs.filter(content__icontains=query)
        return qs

    # def get_object(self):
    #     request = self.request
    #     passed_id = request.GET.get('id',None) or self.passed_id
    #     queryset  = self.get_queryset()
    #     obj = None
    #     if passed_id is not None:
    #         obj = get_object_or_404(queryset, id =passed_id)
    #         self.check_object_permissions(request,obj)
    #     return obj

    
    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None

        

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


    # def get(self,request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id',None)
    #     json_data     = {}
    #     body_         = request.body
    #     if is_json(body_): 
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id',None)
    #     print(request.body)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     if passed_id is not None:
    #         return self.retrieve(request, *args, **kwargs)
    #     return super().get(request, *args, **kwargs)

    # def put(self,request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id',None)
    #     json_data     = {}
    #     body_         = request.body
    #     if is_json(body_): 
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id',None)
    #     print(request.data)
    #     requested_id = json_data.get('id')
    #     passed_id = url_passed_id or new_passed_id or requested_id or None
    #     self.passed_id = passed_id
    #     return self.update(request, *args, **kwargs)

    # def patch(self,request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id',None)
    #     json_data     = {}
    #     body_         = request.body
    #     if is_json(body_): 
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id',None)
    #     print(request.body)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     return self.update(request, *args, **kwargs)

    # def delete(self,request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id',None)
    #     json_data     = {}
    #     body_         = request.body
    #     if is_json(body_): 
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id',None)
    #     print(request.body)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     return self.destroy(request, *args, **kwargs)


