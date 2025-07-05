from django.views.decorators.csrf import csrf_exempt
from django.core.validators import RegexValidator
from django.core.files.base import ContentFile
from .tracker_forms import ScreenShotForm
from .tracker_models import ScreenShot
from django.http import JsonResponse
from core.settings import MEDIA_ROOT
from .report import OrderDetail
from tools.driver import Driver
from core.SEC import SMS_API
from kavenegar import *
from .report_models import (
    RequestCustomer as RC,
    OrderCodes as OC
)
import os

@csrf_exempt
def report(request):
    validator = RegexValidator(r'^\d{6,8}$', 'Invalid order_code format. Must be 7 to 12 digits.')
    order_code = request.POST.get('order_code')
    if order_code:
        try:
            validator(order_code)
            data = OrderDetail(order_code).get_order()
        except Exception as e:
            print(e)
            data = {}
    return JsonResponse(data)

@csrf_exempt
def track(request):
    order_code = request.POST.get('order_code')
    oc = OC.objects.filter(orders_number=order_code)
    success = False
    if oc.exists():
        tracking_number = oc.first().tracking_number
        success = True
    else:
        tracking_number = None
    return JsonResponse({
        'status' : 200 if success else 500,
        'tracking_number' : tracking_number,
        'success' : success
    })

@csrf_exempt
def store_tracking_screenshot(request):
    success = False
    # Test Request => curl -d "tracking_code=SIMPLE_CODE" -X POST HOST:PORT
    if request.method == "POST":
        try:
            # Send tracking variables as arg => tools dir
            tracking_code = request.POST.get('tracking_code')
            # Prepare required PNG image screen shot
            res = Driver(tracking_code).run()
            screen_shot = ContentFile(res['img'], name=f"{tracking_code}.png")
            
            # Define variable form_data for sort returned data
            form_data = {
                'orders_number': None,
                'tracking_number': tracking_code,
                'phone_number': None,
                'customer': None,
            }
            
            # Initialize the form with the data
            form = ScreenShotForm(data=form_data)
            
            # Define image required variables => (storage path as img_path & image file name as img_name)
            img_name = screen_shot.name
            img_path = f"{MEDIA_ROOT}/screen_shots/{img_name}"
            
            # Define a remove file function
            def rm_img(confirm):
                if confirm:
                    os.remove(img_path)
                    print(
                        f"\n=> Removed exist file from media directory\n => File name : {img_name}"
                        )
                    
                else:
                    print(
                        f"\n=> Stored new image file to media directory\n > File name : {img_name}"
                        )
                
            # Check for remove older image if exist
            rm_img(1) if os.path.isfile(img_path) else rm_img(0)
            
            # Store returned data with django form
            screenshot_instance = form.save(commit=False)
            screenshot_instance.image.save(f"{tracking_code}.png", screen_shot)
            screenshot_instance.save()
            
            """ Prepare json response dara include: 
                status as (int), result as(dict) & success as(bol)
                variables for return """
            
            status = 200
            success = True
            result = {
                'tracking_code': screenshot_instance.tracking_number,
                'img': screenshot_instance.image.url
            }
            
        except Exception as error:
            print(f"ERROR +>>>\n{error}")
            result = "Internal server error"
            status = 503
    else:
        result = "Forbidden: not allowed method"
        status = 403
    return JsonResponse({
        'status':status,
        'result': result,
        'success': success
    })

@csrf_exempt
def new_code(request):
    status, response = 503, 'error'
    ''' 
    receive required data from request for store new code to db
    and send sms with phone number to customer 
    '''
    order_code = request.POST.get("order_code")
    full_name = request.POST.get("full_name")
    tracking_code = request.POST.get("tracking_code")
    phone_number = request.POST.get("phone_number")
    # create new data object
    obj = OC.objects.all().create(
        orders_number = order_code,
        tracking_number = tracking_code,
        phone_number = phone_number,
        customer = full_name
    )
    # Now sms time!
    try:
        api = KavenegarAPI(SMS_API)
        params = {
            'receptor': phone_number,
            'template': 'kif123Report',
            'token': tracking_code,
            'type': 'sms',
        }
        response = api.verify_lookup(params)
        status = 200
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)

    return JsonResponse({
        'status' : status,
        'data' : "successfuly stored new code! " if status == 200 else "",
        'success': True if status == 200 else False
    })

