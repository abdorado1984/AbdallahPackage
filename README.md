# AbdallahPackage

# Upgrade pip

        python.exe -m pip install --upgrade pip

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

# 1. Uninstall package

            pip uninstall AbdallahRadwanLib

# 2. Update the Version Number in setup info

            setup.py => increase version No

# 3. clear setup info

            rm -rf dist/ build/ *.egg-info

# 4. prepare setup info

            python setup.py bdist_wheel sdist
                    or
            python setup.py bdist_wheel
            python setup.py sdist

# 5. Check dist [optional]

            twine check dist/*

# 6. Copy Files

            Xcopy D:\MyWork\Abdallah\Python\AbdallahPackage\AbdallahRadwanLib C:\Users\abdullah\appdata\local\programs\python\python312\lib\site-packages\AbdallahRadwanLib /E /H /C /I

            Xcopy D:\MyWork\Git\AbdallahPackage\AbdallahRadwanLib C:\Users\Abdallah-Lat5540\appdata\local\programs\python\python312\lib\site-packages\AbdallahRadwanLib /E /H /C /I

# 7. upload your package

            twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
            get my token from my-package-upload-token

# 8. Install the Package\*\*

            pip install AbdallahRadwanLib
                    or
            pip install AbdallahRadwanLib==VersionNumber
                    or
            pip install AbdallahRadwanLib --upgrade
                    or
            pip install dist/AbdallahRadwanLib-1.1-py3-none-any.whl

# 9. clear setup info

            rm -rf dist/ build/ *.egg-info

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
