# utils.py
from django.http import JsonResponse

def json_response(data=None, status=False, message=""):
    response_data = {
        'status': status,
        'message': message,
    }
    if data is not None:
        response_data.update(data)

    return JsonResponse(response_data)
