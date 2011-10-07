import unittest

from __init__ import Middleware

class DummyRequest(object):
    def __init__(self, useragent):
        self.META = {
            'HTTP_USER_AGENT': useragent,
            'HTTP_ACCEPT': ''
        }

def get_requests(agent_list):
    requests = []
    for agent in agent_list:
        request = DummyRequest(agent)
        
        Middleware.process_request(request)
        
        requests.append(request)
    return requests

class TestBrowserInfo(unittest.TestCase):
    def testDesktopWebkit(self):
        user_agents = [
            # Chrome
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.237 Safari/534.10',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.11 Safari/532.9',
            # Safari
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-us) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
            'mozilla/5.0 (macintosh; u; intel mac os x 10_6_6; en-us) applewebkit/533.19.4 (khtml, like gecko) version/5.0.3 safari/533.19.4',
        ]
        
        requests = get_requests(user_agents)
        
        for request in requests:
            self.assertEqual(request.is_webkit, True)
            self.assertEqual(request.is_wide_device, True)
            self.assertEqual(request.is_touch_device, False)
    
    def testDesktopNonWebkit(self):
        user_agents = [
            # Firefox
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; nl; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13',
            'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3',
            'mozilla/5.0 (macintosh; intel mac os x 10.6; rv:2.0b6) gecko/20100101 firefox/4.0b6'
            # IE
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB0.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; GACID=)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; GTB6.4; .NET CLR 1.1.4322; FDM; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Rogers Hi Speed Internet; (R1 1.3))'
        ]
        
        requests = get_requests(user_agents)
        
        for request in requests:
            self.assertEqual(request.is_webkit, False)
            self.assertEqual(request.is_wide_device, True)
            self.assertEqual(request.is_touch_device, False)
    
    def testiPhoneiPodTouch(self):
        user_agents = [
            # Safari 3.1.1 for iPod Touch 2.0
            'Mozilla/5.0 (iPod; U; CPU iPhone OS 2_0 like Mac OS X; de-de) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5A347 Safari/525.20',
            # iPhone 3G version 2.1
            'Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_1 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F136 Safari/525.20',
            # iPhone 4
            'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7',
            # iPhone 5
            'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
        ]
        
        requests = get_requests(user_agents)
        
        for request in requests:
            self.assertEqual(request.is_webkit, True)
            self.assertEqual(request.is_ios_device, True)
            self.assertEqual(request.is_wide_device, False)
            self.assertEqual(request.is_touch_device, True)
    
    def testiOS5(self):
        user_agents = [
            # iPhone 5
            'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
        ]
        
        requests = get_requests(user_agents)
        
        for request in requests:
            self.assertEqual(request.is_ios5_device, True)
    
    def testiPad(self):
        user_agents = [
            'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; es-es) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B405 Safari/531.21.10',
            'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10',
        ]
        
        requests = get_requests(user_agents)
        
        for request in requests:
            self.assertEqual(request.is_webkit, True)
            self.assertEqual(request.is_ios_device, True)
            self.assertEqual(request.is_wide_device, True)
            self.assertEqual(request.is_touch_device, True)

    def testAndroid(self):
        user_agents = [
            #Nexus One
            'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            # HTC Incredible
            'Mozilla/5.0 (Linux; U; Android 2.1-update1; en-us; ADR6300 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17',
            # Droid 2
            'Mozilla/5.0 (Linux; U; Android 2.2; en-us; DROID2 GLOBAL Build/S273) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            # Droid X
            'Mozilla/5.0 (Linux; U; Android 2.1-update1; en-us; DROIDX Build/VZW) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17 480X854 motorola DROIDX',
            # Droid
            'Mozilla/5.0 (Linux; U; Android 2.1-update1; en-us; Droid Build/ESE81) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17',
        ]
        
        requests = get_requests(user_agents)
        
        for request in requests:
            self.assertEqual(request.is_webkit, True)
            self.assertEqual(request.is_android_device, True)
            self.assertEqual(request.is_wide_device, False)
            self.assertEqual(request.is_touch_device, True)

    def testWebOSNarrow(self):
        user_agents = [
            'Mozilla/5.0 (webOS/1.0; U; en-US) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/1.0 Safari/525.27.1 Pre/1.0',
            'Mozilla/5.0 (webOS/1.4.0; U; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Version/1.0 Safari/532.2 Pixi/1.1',
        ]
        
        requests = get_requests(user_agents)
        
        for request in requests:
            self.assertEqual(request.is_webkit, True)
            self.assertEqual(request.is_webos_device, True)
            self.assertEqual(request.is_wide_device, False)
            self.assertEqual(request.is_touch_device, True)

    def testWindowsPhone(self):
        user_agents = [
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6',
        ]
        
        requests = get_requests(user_agents)
        
        for request in requests:
            self.assertEqual(request.is_webkit, False)
            self.assertEqual(request.is_windows_phone_device, True)
            self.assertEqual(request.is_wide_device, False)
            self.assertEqual(request.is_touch_device, True)

    def testKindle2(self):
        user_agents = [
            'Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 600x800)',
        ]
        
        requests = get_requests(user_agents)
        
        for request in requests:
            self.assertEqual(request.is_webkit, False)
            self.assertEqual(request.is_kindle_device, True)
            self.assertEqual(request.is_wide_device, False)
            self.assertEqual(request.is_touch_device, False)

    def testKindle3(self):
        user_agents = [
            'Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/538.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)',
        ]
        
        requests = get_requests(user_agents)
        
        for request in requests:
            self.assertEqual(request.is_webkit, True)
            self.assertEqual(request.is_kindle_device, True)
            self.assertEqual(request.is_wide_device, False)
            self.assertEqual(request.is_touch_device, False)

    def testSimpleDevices(self):
        user_agents = [
            'Nokia7600/2.0 (03.01) Profile/MIDP-1.0 Configuration/CLDC-1.0 (Google WAP Proxy/1.0)',
            'Nokia8310/1.0 (05.11) UP.Link/6.5.0.0.06.5.0.0.06.5.0.0.06.5.0.0.0',
            'MOT-COOL0/00.62 UP.Browser/6.2.3.4.c.1.128 (GUI) MMP/2.0'
        ]
        
        requests = get_requests(user_agents)
        
        for request in requests:
            self.assertEqual(request.is_simple_device, True)
            self.assertEqual(request.is_webkit, False)
            self.assertEqual(request.is_kindle_device, False)
            self.assertEqual(request.is_wide_device, False)
            self.assertEqual(request.is_touch_device, False)
            
    def testNoUA(self):
        class NoUARequest(object):
            META = {}
        
        request = NoUARequest()
        Middleware.process_request(request)
        
        assert not request.is_android_device
        assert not request.is_kindle_device
        assert not request.is_ios_device
        assert not request.is_touch_device
        assert not request.is_simple_device
        assert not request.is_webkit 
        assert not request.is_webos
        assert request.is_wide_device
        assert not request.is_windows_phone_device

if __name__ == '__main__':
    unittest.main()