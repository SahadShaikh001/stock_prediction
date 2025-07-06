from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
def healthz(request):
    return JsonResponse({"status": "ok"})

@api_view(["POST"])
def register(request):
    return JsonResponse({"message": "Register user (not implemented)"})

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def predict(request):
    return JsonResponse({"message": "Prediction placeholder"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def predictions(request):
    return JsonResponse({"message": "List predictions placeholder"})
