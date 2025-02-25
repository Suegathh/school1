from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer, UserRegisterSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from knox.models import AuthToken
from django.contrib.auth.models import User

class AuthenticationView(APIView):
    permission_classes = [AllowAny]
    def post (self, request, *args, **kwargs):
        user = authenticate(username = request.data['username'], password = request.data['password'])
        if user:
            auth_token = AuthToken.objects.create(user)[1]
            print(auth_token)
            return Response({"token": auth_token}, status=200)
        return Response({"Msg": "Wrong credentials"}, status=401)
    
class UserRegisterView(APIView):
    permission_classes = [AllowAny]
    def post (self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.data['password'])
            user.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class StudentView(APIView):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Validation Errors:", serializer.errors)  # Log the validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    # def get(self, request, id):
    #     student = Student.objects.filter(id = id).first()

    #     if not student:
    #         return Response({"Error": "Student not found"}, status=401)
    #     serializer = StudentSerializer(student)
    #     return Response({"Success": "Success"}, status=201)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        student = Student.objects.filter(id=kwargs['id']).first()
        if not student:
            return Response({"Error": "Student not found"}, status=404)
        
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, *args, **kwargs):
        student = Student.objects.filter(id = kwargs['id']).first()

        if not student:
            return Response({"Error": "Student not found"}, status=404)
        student.delete()
        return Response({"Msg": "Success"}, status=200)


class CourseView(APIView):
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        course = Course.objects.filter(id=kwargs['id']).first()
        if not course:
            return Response({"Error": "Course not found"}, status=404)
        
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        course = Course.objects.filter(id=kwargs['id']).first()
        if not course:
            return Response({"Error": "Course not found"}, status=404)
        
        course.delete()
        return Response({"message": "Course deleted successfully"}, status=200)
