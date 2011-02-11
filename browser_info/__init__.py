from simple_devices import simple_devices

class Middleware(object):
    @staticmethod
    def process_request(request):
        if request.META.has_key("HTTP_USER_AGENT"):
            s = request.META["HTTP_USER_AGENT"].lower()
            
            #defaults
            request.is_adnroid_device = False
            request.is_kindle_device = False
            request.is_ios_device = False
            request.is_touch_device = False
            request.is_simple_device = False
            request.is_webkit = False
            request.is_webos = False
            request.is_wide_device = False
            request.is_windows_phone_device = False
            
            if 'applewebkit' in s:
                request.is_webkit = True
            
            
            if 'ipad' in s:
                request.is_ios_device = True
                request.is_touch_device = True
                request.is_wide_device = True
                
            elif 'iphone' in s or 'ipod' in s:
                request.is_ios_device = True
                request.is_touch_device = True
                
            elif 'android' in s:
                request.is_android_device = True
                request.is_touch_device = True
            
            elif 'webos' in s:
                request.is_webos_device = True
                request.is_touch_device = True
            
            elif 'windows phone' in s:
                request.is_windows_phone_device = True
                request.is_touch_device = True
            
            elif 'kindle' in s:
                request.is_kindle_device = True
            
            # Now that all the good devices are out of the way, lets see if this is an old phone.
            
            elif request.META.has_key("HTTP_X_OPERAMINI_FEATURES"):
                request.is_simple_device = True
                
            elif request.META.has_key("HTTP_ACCEPT"):
                s = request.META["HTTP_ACCEPT"].lower()
                if 'application/vnd.wap.xhtml+xml' in s:
                    request.is_simple_device = True
            
            
            elif any([device in s for device in simple_devices]):
                request.is_simple_device = True

            else:
                # assume desktop at this point
                request.is_wide_device = True
            

def add_browser_info(view):
    """ View Decorator that adds a "mobile" attribute to the request which is
        True or False depending on whether the request should be considered
        to come from a small-screen device such as a phone or a PDA"""
    
    def detected(request, *args, **kwargs):
        Middleware.process_request(request)
        return view(request, *args, **kwargs)
    detected.__doc__ = "%s\n[Wrapped by detect_mobile which detects if the request is from a phone]" % view.__doc__
    return detected