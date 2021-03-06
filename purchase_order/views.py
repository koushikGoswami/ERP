from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from authentication.pagination import ErpLimitOffestpagination, ErpPageNumberPagination
from django_filters.rest_framework import filters
from rest_framework import filters


from purchase_order.serializers import (
    PurchaseOrderSerializer,
    PurchaseDetailSerializer,
    PurchaseFreightSerializer,
    PurchaseOrderReadSerializer,
    PurchaseOrderUpdateStatusSerializer



)
from django.contrib.auth.models import User
from purchase_order.models import PurchaseOrderTerms,PurchaseOrderMap,PurchaseOrderFreight,PurchaseOrderDetail,PurchaseOrder

from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime,timedelta,time,date
from django.utils import timezone



class PurchaseOrderReadView(ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('requisition__requisition_map__requisition_no', 'purchase_order_map__purchase_order_no', 'company__company_name',
                     'purchase_order_detail__company_branch__branch_name','purchase_order_detail__storage_location__storage_address',
                     'purchase_order_detail__storage_bin__bin_no','grand_total')

    def get_queryset(self):
        try:
            order_by = self.request.query_params.get('order_by', None)
            field_name = self.request.query_params.get('field_name', None)

            if order_by and order_by.lower() == 'desc' and field_name:
                queryset = PurchaseOrder.objects.all().order_by('-' + field_name)
            elif order_by and order_by.lower() == 'asc' and field_name:
                queryset = PurchaseOrder.objects.all().order_by(field_name)
            else:
                queryset = PurchaseOrder.objects.all().order_by('-id')
            return queryset

        except Exception as e:
            raise



class PurchaseOrderReadDetailView(RetrieveAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]





class PurchaseOrderReadDropdown(ListAPIView):
    queryset = PurchaseOrder.objects.filter(status=True, is_approve=1, is_finalised=0)
    serializer_class = PurchaseOrderReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]


class PurchaseOrderMatser(ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]



class PurchaseOrderUpdate(RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]

class PurchaseOrderByRequisition(ListAPIView):
    serializer_class = PurchaseOrderReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        requisition=self.kwargs['requisition']
        return PurchaseOrder.objects.filter(requisition_id=requisition,status=True)
    # def get_queryset(self):
    #     requisition=self.kwargs['requisition']
    #     return PurchaseOrder.objects.filter(requisition_id=requisition)



class PurchaseOrderUpdateStatus(RetrieveUpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderUpdateStatusSerializer



class PurchaseOrderSearchView(ListAPIView):

    serializer_class = PurchaseOrderReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination

    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()

        company = self.request.query_params.get('company', None)
        status = self.request.query_params.get('status', None)
        approve=self.request.query_params.get('approve', None)
        from_date=self.request.query_params.get('from_date', None)
        to_date=self.request.query_params.get('to_date', None)
        created_at=self.request.query_params.get('created_at', None)
        vendor=self.request.query_params.get('vendor', None)

        if company is not None:
            queryset = queryset.filter(company_id=company)

        if status is not None:
            queryset = queryset.filter(status=status)

        if approve is not None:
            queryset = queryset.filter(is_approve=approve)

        if vendor is not None:
            queryset = queryset.filter(vendor_id=vendor)

        if created_at is not None:

            created_from_date = datetime.strptime(created_at, "%Y-%m-%d").date()
            created_from_date = datetime.combine(created_from_date, time.min)
            created_from_date = datetime.isoformat(created_from_date)

            created_to_date = datetime.strptime(created_at, "%Y-%m-%d").date()
            created_to_date = datetime.combine(created_to_date, time.max)
            created_to_date = datetime.isoformat(created_to_date)

            queryset = queryset.filter(created_at__gte=created_from_date,created_at__lte=created_to_date)


        if from_date and to_date is not None:

            created_from_date = datetime.strptime(from_date, "%Y-%m-%d").date()
            created_from_date = datetime.combine(created_from_date, time.min)
            created_from_date = datetime.isoformat(created_from_date)

            created_to_date = datetime.strptime(to_date, "%Y-%m-%d").date()
            created_to_date = datetime.combine(created_to_date, time.max)
            created_to_date = datetime.isoformat(created_to_date)

            queryset = queryset.filter(created_at__gte=created_from_date,created_at__lte=created_to_date)

        return queryset



