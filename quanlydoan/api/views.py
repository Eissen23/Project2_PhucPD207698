from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sinhvien, Giangvien, Nhom, Mongiangvien, Thanhviennhom, Cuochop, Report
from .serializers import UserSerializer, SinhvienSerializer, GiangvienSerializer, NhomSerializer, ThanhVienNhomSerializer, CuocHopSerializer, MonGiangVienSerializer, ReportSerializer
from django.contrib.auth import get_user_model
import traceback
import random, string

User = get_user_model()

# Create your views here.
#TODO: Lack of scheduled meet setting,lack of grouping  

def id_generator (size = 5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def insert_student(requested_data, user, fullName, email):
    hoten = fullName
    emailsv = email
    masv = requested_data['code']
    malop = requested_data['malop']
    sdt = requested_data['sdt']
    nganh= requested_data['domain']
    user_id = user
    
    sinhvien = Sinhvien(masv = masv, hoten = hoten,malop=malop ,emailsv = emailsv, sdt = sdt, nganh= nganh, user_id = user_id)
    sinhvien.save()
    
    return sinhvien

def insert_teacher(requested_data, user, fullName, email):
    magv = requested_data['code']
    hotengb = fullName
    teacher_email = email
    vien =  requested_data['domain']
    user_id = user
    
    giangvien = Giangvien(magv = magv, hotengb = hotengb, email = teacher_email, vien = vien, user_id = user_id)
    giangvien.save()
    
    return giangvien

class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request):
        try:
            data = request.data
            
            fullName = data['fullName']
            email = data['email']
            email = email.lower()
            password = data['password']
            re_password = data['re_password']
            
            # TODO: the logic in the signup
            is_teacher = data['is_teacher']
            
            if password ==  re_password:
                if len(password) >= 8:
                    if not User.objects.filter(email=email).exists():
                        if not is_teacher: 
                            user = User.objects.create_user(fullName=fullName, email=email, password=password)
                            insert_student(requested_data=data, user= user, fullName= fullName, email=email)
                            return Response(
                                {"success": "User successfully created"},
                                status= status.HTTP_201_CREATED
                            )
                        else: 
                            teacher = User.objects.create_teacher(fullName=fullName, email=email, password=password)
                            insert_teacher(requested_data=data, user = teacher, fullName=fullName, email=email)
                            return Response(
                                {"success": "Teacher successfully created"},
                                status= status.HTTP_201_CREATED
                            )
                    else:
                        return Response(
                        {'error': 'Email already exist'},
                        status= status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                    {'error': 'Password must have more than 8 character'},
                    status= status.HTTP_400_BAD_REQUEST
                    )
                    
            else:
                return Response(
                    {'error': 'Password do not match'},
                    status= status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            traceback.print_exc()
            return Response(
                {'error': 'Something went wrong!'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
     
class RetrieveUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)
            user_id = user.data['id']
            
            if not user.data['is_teacher']:
                user_detail = Sinhvien.objects.get(user_id = user_id) 
                detail = SinhvienSerializer(user_detail)
                
            else:
                user_detail = Giangvien.objects.get(user_id = user_id)
                detail = GiangvienSerializer(user_detail)
            
            return Response(
                {
                    'user': user.data,
                    'detail': detail.data
                },
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            traceback.print_exc()
            return Response(
                {'error': 'Something went wrong'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
class ManageClass(APIView):
    
    serializer_class = MonGiangVienSerializer
    
    def get(self, request, format = None):
        try:
            user = request.user
            if not user.is_teacher:
                return Response({'error': 'User does not have necessary permission' }, status=status.HTTP_403_FORBIDDEN)
            
            giangvien = Giangvien.objects.get(user_id = user.id)
            giangvien_id = giangvien.magv
            
            mongiangday = Mongiangvien.objects.filter(magv = giangvien_id)
            mongiangday = MonGiangVienSerializer(data=mongiangday, many = True)
            mongiangday.is_valid()
            
            return Response({'classes': mongiangday.data}, status= status.HTTP_200_OK)
                       
        except:
            traceback.print_exc()
            return Response(
                {'error': 'Something went wrong'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        


# get the data of the corresponding user
"""
Để từ giảng viên tới được danh sách các nhóm mà mình quảng lý:
1. từ UserAccount id -> Giangvien user_id VD: giangvien.objects.get(user_id = ...)
2. từ Giangvien magv -> MonGiangVien magv: MonGiangVien.objects.filter(magv = ...)
3. filter lần lượt các nhóm có MonGiangvien magiangday -> Nhom magiangday: Nhom.objects.filter(magiangday = ..)
"""
 
class ManageProjectGroup(APIView):
    
    serializer_class = NhomSerializer
    
    def post(self, request):
        try:
            user = request.user
            
            if not user.is_teacher:
                return Response({'error': 'User does not have necessary permission' }, status=status.HTTP_403_FORBIDDEN)
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                while True: 
                    idnhom = id_generator()
                    if (Nhom.objects.filter(idnhom = idnhom).count() == 0):
                        break                        
                    
                term = serializer.data.get('term') 
                tennhom = serializer.data.get('tennhom')
                tendetai = serializer.data.get('tendetai')
                magiangday = serializer.data.get('magiangday')
                magiangday = Mongiangvien.objects.get(magiangday = magiangday)
                
                nhom = Nhom(idnhom = idnhom, term = term, tennhom = tennhom, tendetai = tendetai, projectstatus = True, magiangday= magiangday )
                nhom.save()
                
                return Response(NhomSerializer(nhom).data, status=status.HTTP_201_CREATED)
            
            return  Response({'error': 'Something went wrong'}, status= status.HTTP_400_BAD_REQUEST)
            
        except :
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # get the list of project group for each the student and teacher
    def get(self, request, format=None):
        try:
            user = request.user
            
            idnhom = request.query_params.get('idnhom')
            project_group = []
            
            # for the teacher side
            if user.is_teacher:   
                giangvien = Giangvien.objects.get(user_id = user.id)
                giangvien_id = giangvien.magv
                
                # incase there is no param idnhom            
                
                
                if not idnhom:
                    mongiangday = Mongiangvien.objects.order_by('mamon').filter(magv = giangvien_id)   
                    mongiangday = MonGiangVienSerializer(data=mongiangday, many = True)
                    
                    mongiangday.is_valid()                
                    for subject in mongiangday.data:
                        nhom = Nhom.objects.get(magiangday = subject.get('magiangday'))
                        # print(NhomSerializer(nhom).data)
                        project_group.append(NhomSerializer(nhom).data)
                            

                    return Response({'nhom': project_group}, status=status.HTTP_200_OK)
                    
                # for incase need to use the param idnhom 
                # check the following vid https://www.youtube.com/watch?v=N5x1wugptUM&list=PLJRGQoqpRwdfgaQujSZMzrG7AkRlbjRkC&index=7
            
            # TODO: test this branch later 
            else:
                sinhvien = Sinhvien.objects.get(user_id = user.id)
                sinhvien_id = sinhvien.masv
                
                if not idnhom:
                    thanhviennhom =  Thanhviennhom.objects.filter(masv = sinhvien_id)
                    thanhviennhom = ThanhVienNhomSerializer(data=thanhviennhom, many = True)
                    
                    thanhviennhom.is_valid()
                    for group in thanhviennhom.data:
                        print(group)
                        nhom = Nhom.objects.get(idnhom = group.get('idnhom'))
                        print(NhomSerializer(nhom).data)
                        project_group.append(NhomSerializer(nhom).data)

                    return Response({'nhom': project_group}, status=status.HTTP_200_OK)
            
        except:
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
            
# handling the member of the group project 
"""
    Để đến được thành viên nhóm:
    
"""       
class ManageStudentGroup(APIView):

    serializer_class = ThanhVienNhomSerializer
    def post(self, request):
        try:
            
            user = request.user
            
            if not user.is_teacher:
                return Response({'error': 'User does not have necessary permission' }, status=status.HTTP_403_FORBIDDEN)
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                while True:
                    mathamgia = id_generator(size=8)
                    if(Thanhviennhom.objects.filter(mathamgia = mathamgia).count() == 0):
                        break
                    
                masv = serializer.data.get('masv')
                masv = Sinhvien.objects.get(masv = masv)
                
                idnhom = serializer.data.get('idnhom')
                idnhom = Nhom.objects.get(idnhom = idnhom)
                
                tvn = Thanhviennhom(mathamgia = mathamgia, masv = masv, idnhom = idnhom)
                tvn.save()  

                return Response(ThanhVienNhomSerializer(tvn).data, status=status.HTTP_201_CREATED)
            
            return Response({'error': 'Something went wrong'}, status= status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request, format= None):
        user = request.user
        


class CreateMeeting(APIView):
    serializer_class = CuocHopSerializer
    
    def post(self, request):
        try: 
            user= request.user
            if not user.is_teacher:
                return Response({'error': 'User does not have necessary permission' }, status=status.HTTP_403_FORBIDDEN)
            
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                while True:
                    id = id_generator(size=10)
                    if (Cuochop.objects.filter(id = id).count() == 0):
                        break
                    
                idnhom = serializer.data.get('idnhom')
                idnhom = Nhom.objects.get(idnhom = idnhom)
                
                meettime = serializer.data.get('meettime')
                isreported = serializer.data.get('isreported')
                ghichu = serializer.data.get('ghichu')

                cuochop = Cuochop(id = id, idnhom = idnhom, meettime = meettime, isreported = isreported, isscheduled = True, ghichu = ghichu)
                cuochop.save()
                
                if isreported:
                    while True:
                        reportid= id_generator(size=10)
                        if(Report.objects.filter(reportid = reportid).count() == 0):
                            break
                        
                    report = Report(reportid = reportid, codeurl= "", report = "", cuochop = cuochop)
                    report.save()
                
                return Response(CuocHopSerializer(cuochop).data, status=status.HTTP_201_CREATED)
            
            return Response({'error': serializer.errors}, status= status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request, format = None):
       try:
            user = request.user
            
            data = request.data 
            idnhom = data['idnhom']
            
            nhom = Nhom.objects.get(idnhom = idnhom)
            meeting = Cuochop.objects.get(idnhom = nhom.idnhom)
            meeting = CuocHopSerializer(data = meeting, many = True)
            meeting.is_valid
            
            return Response({'last_meeting': meeting.data},status= status.HTTP_200_OK)
       except:
            traceback.print_exc()
            return Response({'error': meeting.errors}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ManageReport(APIView):
    def put(self, request):
        try:
            user = request.user
            if user.is_teacher: 
                return Response({'error':'Only student are allowed'}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            
            meeting_id = data['id']
            
            codeurl = data['codeurl']
            report = data['report']
            
            baocao = Report.objects.filter(cuochop = meeting_id).update(reportid = baocao.id,codeurl = codeurl, report = report, cuochop=meeting_id)
       
            return Response(
                {'success': 'Listing updated successfully'},
                status=status.HTTP_200_OK
            )
            
        except: 
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)