from setuptools import find_packages
from setuptools import setup

version = '0.0.1dev0'

setup(
    name='collective.statusview',
    version=version,
    description=(
        'This Plone add-on provides a configurable status view.'
    ),
    long_description=(
        open('README.rst').read() + '\n' +
        open('CHANGES.rst').read() + '\n'
    ),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: 5.0',
        'Framework :: Plone :: 5.1',
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
    ],
    keywords='',
    author='',
    author_email='',
    url='https://github.com/collective/collective.statusview',
    license='GPLv2',
    packages=find_packages(),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.CMFPlone',
        'plone.api >=1.0.0,<=1.99.99',
        'plone.app.registry',
        'setuptools',
        'z3c.autoinclude',
    ],
    extras_require={
        'test': [
            'plone.app.testing'
        ]
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """
)
