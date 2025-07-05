from core.SEC import WC_API

class OrderDetail:
    def __init__(self, order_code):
        self.ctx = {}
        self.order_code = int(order_code)
        
    def get_order(self):
        response = WC_API.get(f'orders/{self.order_code}').json()
        if response.get('status') is not None:
            # personal details
            status = response['status']
            if status == 'completed':
                self.ctx['status'] = 'تکمیل پردازش و خروج از انبار های ۱۲۳ کیف'
            elif status == 'processing':
                self.ctx['status'] = 'در حال پردازش سفارش'
            elif status == 'pending':
                self.ctx['status'] = 'در انتظار پرداخت'
            elif status == 'cancelled':
                self.ctx['status'] = 'لغو شده'
            elif status == 'on-hold':
                self.ctx['status'] = 'در انتظار برسی'
            else:
                self.ctx['status'] = response['status'] 
            first_name = response['shipping']['first_name'] if response['shipping']['first_name'] is not None else ""
            last_name = response['shipping']['last_name'] if response['shipping']['last_name'] is not None else ""
            self.ctx['full_name'] = f"{first_name} {last_name}"
            # billing / shipping details
            city = response['billing']['city'] if response['billing']['city'] is not None else ""
            phone = response['billing']['phone'] if response['billing']['phone'] is not None else ""
            address = response['billing']['address_1'] if response['billing']['address_1'] is not None else ""
            unit = response['billing']['address_2'] if response['billing']['address_2'] is not None else ""
            postcode = response['shipping']['postcode'] if response['shipping']['postcode'] is not None else ""
            self.ctx['shipping_method'] = response['shipping_lines'][0]['method_title'] if response.get('shipping_lines') and len(response['shipping_lines']) > 0 else ""
            self.ctx['shipping_total'] = response['shipping_lines'][0]['total'] if response.get('shipping_lines') and len(response['shipping_lines']) > 0 else ""
            self.ctx['full_address'] = f"شهر {city} / {address} / {unit} / کدپستی: {postcode}"
            # invoke details
            if status == "completed" or status == "processing" or status == "cancelled":
                self.ctx['products'] = [{
                    'name': i[0].split(' - ')[0] if i[0].split(' - ') is not None else "",
                    'color': i[0].split(' - ')[1] if i[0].split(' - ') is not None else "",
                    'qty': i[1].split(" ")[1] if i[1].split(" ") is not None else ""
                    }for i in [
                        x.split('&times;') for x in response['shipping_lines'][0]['meta_data'][0]['display_value'].split(',')
                        ]]
            self.ctx['payment_method_title'] = response['payment_method_title'] if response['payment_method_title'] is not None else ""
            self.ctx['total'] = response['total'] if response['total'] is not None else ""
            
        return self.ctx