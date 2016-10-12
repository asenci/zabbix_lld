from setuptools import setup, find_packages

setup(
    name='zabbix_lld',
    description='Low level discovery functions for Zabbix',
    version='0.2',
    author='Andre Sencioles',
    author_email='asenci@gmail.com',
    license='ISC License',
    url='https://bitbucket.org/asenci/zabbix_lld',

    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'zabbix_lld = zabbix_lld:main',
        ]
    },
)
