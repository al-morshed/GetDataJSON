from django.http import Http404
from django.shortcuts import render, redirect
import datetime

# Create your views here.
from django.utils import timezone
from rest_framework.decorators import api_view

from .forms import AddForm


def home(request):
    context = {
        'title': 'Index',
        #        'posts':services.objects.all()
    }
    return render(request, 'index.html', context)


# -------------------------------------------
from .serializers import (
    ListSerializer,
    AddSerializer,
    ShowSerializer,
    DeleteSerializer,
    postSerializer,
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)

from customer.models import Partner


class LicenseListAPIView(ListAPIView):
    serializer_class = ListSerializer
    queryset = Partner.objects.all()
# queryset = Partner.objects.filter(active=False)

from django.views.decorators.csrf import csrf_exempt
# @api_view(['POST', ])
@csrf_exempt
def add(request):
    form = AddForm(request.POST)
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            # post_saved = form.save(active=True)
            # post_saved = form.save(commit=False)
            # post_saved.author = request.user.id
            form.save()
    return render(request, 'add.html', {'form': form, })


class AddLicense(CreateAPIView):
    def get_queryset(self):
        RouterSerial = self.kwargs['RouterSerial']
        # print(self.kwargs)
        print(RouterSerial)
        qs = Partner.objects.filter(RouterSerial=RouterSerial)
        if not qs:
            serializer_class = AddSerializer
        serializer_class = None
    queryset = Partner.objects.all()
    serializer_class = AddSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = AddSerializer(data=request.data, context={"request": request})  # change here
        print("RouterSerial")
        print(request.data)
        # if request.data["adduser"]: pass

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response(all)

    def perform_create(self, serializer):
        # By print(self.request.data, serializer.validated_data), you can check how serializer validation discards
        # extra or read only fields even if you give it.
        serializer.save()  # in BaseSerializer.save(), this kwarg is added to validatd_data
from rest_framework.response import Response

from datetime import datetime
class ShowLicense(RetrieveAPIView):
    serializer_class = ShowSerializer
    lookup_field = str('RouterSerial')
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        RouterSerial = self.kwargs['RouterSerial']
        print(RouterSerial)
        if not Partner.objects.filter(RouterSerial=RouterSerial)[0].log:
            Partner.objects.filter(RouterSerial=RouterSerial).update(log=1, last_login_date=datetime.now())
        else:
            Partner.objects.filter(RouterSerial=RouterSerial).update(
                log=Partner.objects.filter(RouterSerial=RouterSerial)[0].log + 1, last_login_date=datetime.now())

        return Partner.objects.filter(RouterSerial=RouterSerial)
   # return Response(serializer.data)
    # def get(self, request,serializer):
    # 	allpost = Partner.objects.all()
    # 	serializer_class = ShowSerializer
    # 	#updateaDta(request)
    # 	lookup_field = str('RouterSerial')
    # 	serializer = userSerializer(serializer_class, many=True)
    # 	return Response(serializer.data)
    # queryset = Partner.objects.all()

class DeleteLicense(DestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = DeleteSerializer
    lookup_field = 'RouterSerial'


from rest_framework.views import APIView
from rest_framework.response import Response
from customer.models import Partner, Post
from .serializers import userSerializer


class userList(APIView):

    def get(self, request):
        allpost = Partner.objects.all()
        serializer = userSerializer(allpost, many=True)
        return Response(serializer.data)

    def post(self):
        pass

from .serializers import postSerializer
class postList(ListAPIView):
    # queryset = Post.objects.all()
    # serializer_class=postSerializer
    serializer_class = ListSerializer
    queryset = Post.objects.all()

from rest_framework import status
class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Partner.objects.get(pk=pk)
        except Partner.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        partner = self.get_object(pk)
        serializer = userSerializer(partner)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = userSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth.forms import UserCreationForm
# from customer.forms import RegisterForm
# from customer.models import DriverUs
# def register(request):
#
# 	if request.user.is_authenticated:
# 		return redirect('admin:logout')
# 	else:
# 		if request.method == 'POST':
# 			form = RegisterForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				return redirect('customer:list')
# 		else:
# 			form = RegisterForm()
#
# 			args = {'form':form}
# 			return render(request, 'customer/register.html', args)
