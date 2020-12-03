import setuptools

setuptools.setup(
    name='npm-register-cli',
    version='2020.12.3',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/npm-register']
)
