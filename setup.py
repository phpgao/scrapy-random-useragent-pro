from setuptools import setup

from scrapy_random_useragent_pro import VERSION

setup(
    name='scrapy-random-useragent-pro',
    version=VERSION,
    url='https://github.com/phpgao/scrapy-random-useragent-pro',
    description='A random user-agent for all your needs',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    keywords='random useragent scrapy middleware',
    license='MIT License',
    author="Jimmy",
    author_email='endoffight@gmail.com',
    install_requires=[
        'scrapy >= 1.0.0'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Scrapy',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=[
        'scrapy_random_useragent_pro',
    ],
)
