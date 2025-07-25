import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from meetings.serializers import CuocHopSerializer, ReportSerializer
from quanlydoan.api.models import Nhom
from quanlydoan.api.utilities import id_generator
from .models import Cuochop, Report


# Create your views here.
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
            
        except Exception:
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request, format = None):
       try:
            
            data = request.data 
            idnhom = data['idnhom']
            
            nhom = Nhom.objects.get(idnhom = idnhom)
            meeting = Cuochop.objects.filter(idnhom = nhom.idnhom)
            meeting = CuocHopSerializer(data = meeting, many = True)
            meeting.is_valid()
            
            return Response({'last_meeting': meeting.data},status= status.HTTP_200_OK)
       except Exception:
            traceback.print_exc()
            return Response({'error': "something wrong"}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ManageReport(APIView):
    def put(self, request):
        try:
            user = request.user
            if user.is_teacher: 
                return Response({'error':'Only student are allowed'}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            
            meeting_id = data['id']
            meeting = Cuochop.objects.get(id = meeting_id)
            
            codeurl = data['codeurl']
            report = data['report']
            
            baocao = Report.objects.filter(cuochop = meeting)

            baocao.update(reportid = baocao.id,codeurl = codeurl, report = report, cuochop=meeting)

            return Response(
                {'success': 'Listing updated successfully'},
                status=status.HTTP_200_OK
            )
            
        except Exception: 
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
    def get(self, request, format = None):
        try:
            user = request.user
            if not user.is_teacher:
                return Response({'error':'Only student are allowed'}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            meeting_id = data['cuochop']
            meeting = Cuochop.objects.get(id = meeting_id)
            
            
            report = Report.objects.filter(cuochop = meeting)
            report = ReportSerializer(data = report)
            report.is_valid()
            
            return Response({'data': report.data}, status=status.HTTP_200_OK)
            
        except Exception:
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)