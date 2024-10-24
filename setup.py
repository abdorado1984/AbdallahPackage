from setuptools import setup, find_packages

setup(
    name='AbdallahRadwanLib',
    version='0.8',    
    description='My First Package for Python Projects with PyPI Package - October 2024',  
    # package_dir={"": "app"},
    # packages=find_packages(where="app"),
    packages=find_packages(),
    include_package_data=True,  # Includes non-code files if specified in MANIFEST.in
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/abdorado1984/AbdallahPackage',
    author='Abdallah Radwan',
    author_email='AbdallahRadwan2011@gmail.com',    
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",        
    ],    
    python_requires='>=3.12',   
)

# packages=['arUtilities'],
