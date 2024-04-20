from setuptools import setup, find_packages

setup(
   name='my_project_2',
   version='1.0',
   description='For vector operations',
   license='MIT',
   author='Oksana Galiulina',
   author_email='oksana17.06@bk.ru',
   url='https://github.com/mgwoorl/my_project2',
   packages=find_packages(exclude=['test']), 
   install_requires=['numpy'],
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
