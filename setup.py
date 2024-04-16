from setuptools import setup

setup(
   name='vector_operations',
   version='1.0',
   description='For vector operations',
   license='MIT',
   author='Oksana Galiulina',
   author_email='oksana17.06@bk.ru',
   url='https://github.com/mgwoorl/my_project2',
   packages=['code'], 
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
