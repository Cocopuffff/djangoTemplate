from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskSerializer
from .models import Task
from rest_framework_simplejwt.authentication import JWTAuthentication


class TaskList(APIView):

    permission_classes = (IsAuthenticated,)
    # get method - up to 4 methods
    def get(self, request):
        # get the task class
        tasks = Task.objects.all()
        # serialize all tasks (many=True makes it serialize all)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class TaskDetails(APIView):
    def get(self, request, pk):
        # get by id request with id url params
        tasks = Task.objects.get(id=pk)
        serializer = TaskSerializer(tasks, many=False)
        return Response(serializer.data)


class TaskCreate(APIView):
    def put(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class TaskUpdate(APIView):
    def patch(self, request, pk):
        task = Task.objects.get(id=pk)
        # instance=task from database, data=request.data is the user's json body,
        # partial=True means data that comes in does not need to exactly match the entire row in the database
        serializer = TaskSerializer(instance=task, data=request.data, partial=True)

        # django requires you to validate serializer before saving
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class TaskDelete(APIView):
    def delete(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()

        return Response('item deleted')


class JwtDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        response = JWTAuthentication().authenticate(request)
        if response is not None:
            account, token = response

            print(account)
            print(account.id)

            return Response(token.payload)