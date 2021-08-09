from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from myapp.models import Reporter
from .serializers import ReporterSerializers
import time
# Create your views here.

# List all reporter
# R trong CURD
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def api_all_reporter(request):
    reporters = Reporter.objects.all()
    mydata = ReporterSerializers(reporters, many=True)
    # results = []
    # for reporter in reporters:
    #     results.append({
    #         'first_name': reporter.first_name,
    #         'last_name': reporter.last_name,
    #         'email': reporter.email,
    #         'id': reporter.id
    #     })
    time.sleep(3)
    return Response(data=mydata.data, status=200)

@api_view(["GET"])
@permission_classes((IsAuthenticated, ))
def api_view_reporter(request, reporter_id):
    try:
        reporter = Reporter.objects.get(id=reporter_id)
        # result = {
        #     'first_name': reporter.first_name,
        #     'last_name': reporter.last_name,
        #     'email': reporter.email,
        # }
        mydata = ReporterSerializers(reporter)
        return Response(data=mydata.data, status=200)
    except Reporter.DoesNotExist:
        return Response(data={"message": f"Report id {reporter_id} not found !"}, status=404)

# C trong CURD
@api_view(["POST"])
@permission_classes((IsAuthenticated, ))
def api_add_reporter(request):
    data = ReporterSerializers(data = request.data)
    if data.is_valid():
        print(data.validated_data)
        data.save()
        return Response(data={
        "message": f"Reporter id created : {dict(data.validated_data)}"
    }, status=201)
    # created_id = Reporter.objects.create(**request.data)
    else:
        print(data.errors)
        return Response(data={
            "message": data.errors
        }, status=400)

# U trong CURD
@api_view(["PUT"])
@permission_classes((IsAuthenticated, ))
def api_update_reporter(request, reporter_id):
    if list(request.data.keys()) != ['first_name', 'last_name', 'email']:
        return Response(data={"message": f"Error with your data"}, status=400)
    else:
        try:
            reporter = Reporter.objects.get(id=reporter_id)
            reporter.first_name = request.data['first_name']
            reporter.last_name = request.data['last_name']
            reporter.email = request.data['email']
            reporter.save()
            result = {
                'first_name': reporter.first_name,
                'last_name': reporter.last_name,
                'email': reporter.email,
            }
            return Response(data={
                "message": f"Update reporter id {reporter_id} successful.",
                "data": result
            }, status=200)
        except Reporter.DoesNotExist:
            return Response(data={"message": f"Report id {reporter_id} not found !"}, status=404)

@api_view(["PATCH"])
@permission_classes((IsAuthenticated, ))
def api_patch_reporter(request, reporter_id):
    try:
        reporter = Reporter.objects.get(id=reporter_id)
        reporter.first_name = request.data.get('first_name',reporter.first_name )
        reporter.last_name = request.data.get('last_name',reporter.last_name  )
        reporter.email = request.data.get('email', reporter.email )
        reporter.save()
        result = {
            'first_name': reporter.first_name,
            'last_name': reporter.last_name,
            'email': reporter.email,
        }
        return Response(data={
            "message": f"Update reporter id {reporter_id} successful.",
            "data": result
        }, status=200)
    except Reporter.DoesNotExist:
        return Response(data={"message": f"Report id {reporter_id} not found !"}, status=404)
# D trong CURD
@api_view(["DELETE"])
@permission_classes((IsAuthenticated, ))
def api_delete_reporter(request, reporter_id):
    try:
        reporter = Reporter.objects.get(id=reporter_id)
        reporter.delete()
        return Response(data={
            "message": "Delete succesful"
        }, status=204)
    except Reporter.DoesNotExist:
        return Response(data={"message": f"Report id {reporter_id} not found !"}, status=404)
    

class ReporterListAPI(APIView):
    # Các gì ảnh hưởng List data thì để vào đây ?
    # Hàm của view mà ko có tham số
    
    # GET all
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        reporters = Reporter.objects.all()
        results = []
        for reporter in reporters:
            results.append({
                'first_name': reporter.first_name,
                'last_name': reporter.last_name,
                'email': reporter.email,
                'id': reporter.id
            })
        time.sleep(3)
        return Response(data=results, status=200)

    # POST 
    def post(self, request):
        created_id = Reporter.objects.create(**request.data)
        return Response(data={
            "message": f"Reporter id created : {created_id}"
        }, status=201)

class ReporterAPI(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, reporter_id):
        print("GET ReporterAPI")
        try:
            reporter = Reporter.objects.get(id=reporter_id)
            result = {
                'first_name': reporter.first_name,
                'last_name': reporter.last_name,
                'email': reporter.email,
            }
            return Response(data=result, status=200)
        except Reporter.DoesNotExist:
            return Response(data={"message": f"Report id {reporter_id} not found !"}, status=404)

    def put(self, request, reporter_id):
        if list(request.data.keys()) != ['first_name', 'last_name', 'email']:
            return Response(data={"message": f"Error with your data"}, status=400)
        else:
            try:
                reporter = Reporter.objects.get(id=reporter_id)
                reporter.first_name = request.data['first_name']
                reporter.last_name = request.data['last_name']
                reporter.email = request.data['email']
                reporter.save()
                result = {
                    'first_name': reporter.first_name,
                    'last_name': reporter.last_name,
                    'email': reporter.email,
                }
                return Response(data={
                    "message": f"Update reporter id {reporter_id} successful.",
                    "data": result
                }, status=200)
            except Reporter.DoesNotExist:
                return Response(data={"message": f"Report id {reporter_id} not found !"}, status=404)

    def delete(self, request, reporter_id):
        try:
            reporter = Reporter.objects.get(id=reporter_id)
            reporter.delete()
            return Response(data={
                "message": "Delete succesful"
            }, status=204)
        except Reporter.DoesNotExist:
            return Response(data={"message": f"Report id {reporter_id} not found !"}, status=404)

    def patch(self, request, reporter_id):
        try:
            reporter = Reporter.objects.get(id=reporter_id)
            reporter.first_name = request.data.get('first_name',reporter.first_name )
            reporter.last_name = request.data.get('last_name',reporter.last_name  )
            reporter.email = request.data.get('email', reporter.email )
            reporter.save()
            result = {
                'first_name': reporter.first_name,
                'last_name': reporter.last_name,
                'email': reporter.email,
            }
            return Response(data={
                "message": f"Update reporter id {reporter_id} successful.",
                "data": result
            }, status=200)
        except Reporter.DoesNotExist:
            return Response(data={"message": f"Report id {reporter_id} not found !"}, status=404)

# Http methods
# GET,POST,PUT,PATCH,DELETE,OPTIONS....

# Method : GET : list all/view detail: Lấy hết tất cả hoặc lấy 1 object
# Response: 
    # HTTP Status code: 200 OK -> thành công
    #                 : 404 Not Found -> Đường dẩn này không tồn tại hoặc
    #                                    Object không tìm thấy


# Method: POST : Tạo mới 1 object / create/insert data
# Response: 
    # Code: 201 Created -> object tạo thành công/insert thành công
    #       409 Conflict -> Tạo không thành công: trùng lặp data
    #       400 Bad Request -> Data gửi lên không đúng format


# Method: PUT : Mình muốn cập nhật 1 object (phải có đầy đủ tất cả các thông tin của object đó)
# Response:
    # Code : 200 OK
    #        204: No content 
    #        404 Not Found
    #        400 Bad Request -> Data gửi lên không đúng format

# Method: PATCH : Cập nhật 1 object (không cần phải có đầy đủ thông tin của đối tượng. Trong data của mình có gì thì cập nhật cái đó)
# Response:
    # Code : 200 OK
    #        204: No content 
    #        404 Not Found
    #        400 Bad Request -> Data gửi lên không đúng format

# Ví du: Object first_name, last_name, email.
# PUT -> Gửi object gồm đầy đủ 3 thông tin trên
# PATCH -> Muốn cập nhất first_name thì gửi first_name.

# Method DELETE: Detroy object / xoá object
# Response:
    # Code : 200 OK
    #        204: No content 
    #        404 Not Found

# Method OPTIONS -> nhiệm vụ là kiễm tra phía server chấp nhận những method nào/ header nào.


# Code:
# 1XX -> Information
# 2xx -> Success response
    # 200
    # 201 Created
    # 204 No content
# 3xx -> Redirect
    # 302 Redirect
# 4xx -> Client error
    # 400 Bad request
    # 401 Unauthorized -> Chưa đăng nhập
    # 403 Forbidden -> Chưa đăng nhập/không có quyền truy cập
    # 404 Not found
    # 405 Method Not Allow
    # 408 Request time out
    # 409 Conflict
# 5xx -> Server error
    # 502 Bad Gateway -> Thấy nhiều ở trang đăng ký môn học :))
    # 500 Internal server 
