from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StatusSerializer
from .models import Status
from rest_framework import generics,mixins
from .forms import StatusForm 

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

class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView): #Create and List View
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)





class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'


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


