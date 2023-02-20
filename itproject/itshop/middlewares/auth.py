from django.shortcuts import redirect


def auth_middleware(get_response):
    def middleware(request):
        returnUrl=request.META['PATH_INFO']
        customer=request.session.get('customer')
        if not request.session.get('customer'):
            return redirect(f'login?return_url={returnUrl}')
        response=get_response(request)
        return response

    return middleware(request) 
          
        # print(reqest.META['PATH_INFO'])

