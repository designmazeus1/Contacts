from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Contact
from .serializers import ContactSerializer


class ContactListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer

    # 1. Create
    def post(self, request):
        serializer = ContactSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : True,
                'message' : 'Success',
                'Data' : serializer.data},
                status=status.HTTP_201_CREATED)
        else :
            return Response({
                'status' : False,
                'message' : "Error"},
                status = status.HTTP_400_BAD_REQUEST)

    # 2. List all
    def get(self, request):
        todos = Contact.objects.filter(user=request.user.id)
        serializer = ContactSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class ContactDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer

    def get_object(self, contact_id, user_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Contact.objects.get(id=contact_id, user = user_id)
        except Contact.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, contact_id, *args, **kwargs):

        todo_instance = self.get_object(contact_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ContactSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, contact_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(contact_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'text': request.data.get('text'),
            'image': request.data.get('image'),
            'description': request.data.get('description'),
            'completed': request.data.get('completed'),
            'user': request.user.id
        }
        serializer = ContactSerializer(instance = todo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, contact_id, *args, **kwargs):

        todo_instance = self.get_object(contact_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )