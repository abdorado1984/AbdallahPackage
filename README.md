# AbdallahPackage
**-----------------------------------------------------------**

**Install the following packages**
    pip install twine
    pip install setuptools wheel
    pip install tqdm
        or 
    pip install twine setuptools wheel tqdm

    python setup.py sdist
    twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

**---------------------Update My Package---------------------**

#     1. Uninstall package
            pip uninstall AbdallahRadwanLib
#     2. Update the Version Number in setup info
#     3. clear setup info
            rm -rf dist/ build/ *.egg-info
    
#     4. prepare setup info
            python setup.py bdist_wheel sdist
                    or
            python setup.py bdist_wheel
            python setup.py sdist        

#     5. Check dist [optional]
            twine check dist/*

#     6. upload your package
            twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
            get my token from my-package-upload-token

#     7. Install the Package Locally**
            pip install dist/AbdallahRadwanLib-0.10-py3-none-any.whl
                    or
            pip install AbdallahRadwanLib
                    or
            pip install AbdallahRadwanLib==VersionNumber            
                    or
            pip install AbdallahRadwanLib --upgrade
**-----------------------------------------------------------**

**Reinstall with --force-reinstall and --no-binary**
    pip install --force-reinstall --no-binary=:all: AbdallahRadwanLib

**Download the source manually**
    pip download --no-binary=:all: AbdallahRadwanLib
    tar -xvzf AbdallahRadwanLib-0.6.tar.gz

**View at**
    https://pypi.org/project/AbdallahRadwanLib/0.8/

**-----------------------------------------------------------**

**List of Mibrary file**
    arUtilityConst
    arUtilityEnum
    arUtilitySettings
    arUtilityGeneral
    arUtilityEncryption
    arUtilityFile
    arUtilityConfig
    arUtilityDBOracle
    arUtilityDBSqlAlchemy
**-----------------------------------------------------------**    