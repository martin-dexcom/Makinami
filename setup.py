from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'makinami',
    version = '0.0.1',
    author = 'Martin Garcia',
    author_email = 'martin.garcia@dexcom.com',
    license = 'Apache License 2.0',
    description = 'CLI Wizard Tool to help new hires with their environment setup.',
    long_description = long_description,
    url = 'https://github.com/martin-dexcom/Makinami',
    py_modules = ['my_tool','app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires = '>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_point = '''
        [console_scripts]
        makinami=my_tool:main
    '''
)