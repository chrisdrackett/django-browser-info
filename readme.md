About
=====

This application adds attributes to your request object that describe the users browser. This will let you fine tune the templates or code to use based on the traits of the browser.

The following is currently added to the request:

Simple Device
-------------

	request.is_simple_device

True for all non-desktop devices (browsers) without "modern" CSS and JS support. This includes non "smart" phones and simpler browsers like those found on game consoles and the kindle.

Touch Device
------------

	request.is_touch_device

True for devices that use touch events.

Wide Device
-----------

	request.is_wide_device

True for devices that are wider than a common mobile phone. This covers tablets and desktop browsers.

Device Type
-----------

	request.is_ios_device
	request.is_ios5_device
	request.is_android_device
	request.is_webos_device
	request.is_windows_phone_device
	request.is_kindle_device

True if the device is part of the given platform.

These give more granular information about modern smart devices. This is helpful if you want to target features to a specific device type.

Other Attributes
----------------

	request.is_webkit

True if the browser is webkit (desktop or mobile.)

Installation
============

After you've added browser_info to your python path (manually or with pip) you can access its attributes with one of two methods.

All Requests
------------

To use browser_info on all requests just add

	browser_info.Middleware

to the `MIDDLEWARE_CLASSES` tuple in your settings.py

Specific Requests
-----------------

If you only have certain views that need the distinction all you need to do is wrap the relevant views like this:

	from browser_info import add_browser_info

	@add_browser_info
	def my_mobile_view(request):
		# your view code here.