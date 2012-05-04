from distutils.core import setup
 
setup(
    name='django-browser-info',
    version='1.0.1',
    description='Django middleware and view decorator to add browser info to the request object',
    long_description = open("readme.md").read(),
    author='Chris Drackett',
    author_email='drackett@mac.com',
    url = "https://github.com/chrisdrackett/django-browser-info",
    packages = [
        "browser_info",
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
