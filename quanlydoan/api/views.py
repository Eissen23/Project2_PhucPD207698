from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sinhvien, Giangvien, Nhom, Mongiangvien, Thanhviennhom
from .serializers import NhomSerializer, ThanhVienNhomSerializer, MonGiangVienSerializer
from django.contrib.auth import get_user_model
import traceback
from api.utilities.id_generator import id_generator

User = get_user_model()

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
                       
        except Exception:
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
            
        except Exception:
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
            
        except Exception:
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
            
        except Exception:
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request, format= None):
        pass        
