from setuptools import setup, find_packages

setup(
    name='py0ltv',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'antlr4-python3-runtime',
    ],
    entry_points={
        'console_scripts': [
            'py0=py0.main:main',
        ],
    },
    author='LapTrinhVui',
    author_email='syriackeyboard@gmail.com',
    description='A transpiler for .py0 files to Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ltvtk/py0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    package_data={'py0': ['generated/*.py']},
)