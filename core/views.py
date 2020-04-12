from django.http import JsonResponse

def index(request):
    data = {'status': 'ok', 'msg': 'success'}
    return JsonResponse(data)
