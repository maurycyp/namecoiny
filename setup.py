try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='namecoiny',
    version='0.1.0',
    description='',
    long_description=open('README.txt').read(),
    author='Maurycy Pietrzak',
    author_email=['github.com@wayheavy.com'],
    url='https://github.com/maurycyp/namecoiny',
    packages=['namecoiny'],
    license='Unlicense',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: Name Service (DNS)',
    ],
    install_requires=[
        'docopt==0.6.2',
        'paramiko==1.15.2',
        'six==1.9.0',
        'skiff==0.9.8',
    ],
    entry_points={'console_scripts': [
        'namecoiny = namecoiny.app:main',
    ]},
    # TODO zip_safe, package_data
)
