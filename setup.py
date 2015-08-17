from setuptools import setup

import django_me


setup(name='django-me',
      version=django_me.__version__,
      description=django_me.__doc__,
      author=django_me.__author__,
      url='https://github.com/nixdaemon/django-me',
      license=django_me.__license__,
      platforms=['all'],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: Jython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Django Mongoengine Integration',
      ],
      py_modules=['django_me'],
      )
