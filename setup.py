# -*- coding: utf-8 -*-
"""Setup file for easy installation"""
from os.path import join, dirname
from setuptools import setup, find_packages

version = __import__('flattr').__version__

LONG_DESCRIPTION = """
"""

def long_description():
    """
    """
    try:
        return open(join(dirname(__file__), 'README.md')).read()
    except IOError:
        return LONG_DESCRIPTION


setup(name='django-flattr',
      version=version,
      author='Andreas Neumeier',
      author_email='andreas@neumeier.org',
      description='Django flattr tags.',
      license='BSD',
      keywords='django, flattr, application',
      url='https://github.com/aneumeier/django-flattr',
      download_url='https://github.com/aneumeier/django-flattr',
      packages=['flattr', 'flattr.templatetags',],
      package_data={'flattr': ['locale/*/LC_MESSAGES/*']},
      long_description=long_description(),
      install_requires=['django>=1.3.1', ],
      classifiers=['Framework :: Django',
                   'Development Status :: 4 - Beta',
                   'Topic :: Internet',
                   'License :: OSI Approved :: BSD License',
                   'Intended Audience :: Developers',
                   'Environment :: Web Environment',
                   'Programming Language :: Python :: 2.7'])

