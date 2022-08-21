from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf8') as fd:
    long_description = fd.read()

setup(
    name='budgetter',
    version='2022.1.0',
    packages=find_packages(),
    package_dir={'': 'view/resources'},
    keywords=['finance', 'finance manager', 'budget', 'accounts'],
    entry_points={
        'gui_scripts': [
            'Budgetter = budgetter.main:start_app'
        ]
    },
    url='https://github.com/opierre/Budgetter',
    license='GPL-3.0',
    author='OLIVIER Pierre',
    author_email='pierreolivier.pro@gmail.com',
    description='Budgetter finance manager desktop application',
    long_description=long_description
)
