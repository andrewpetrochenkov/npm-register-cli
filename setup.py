import setuptools

setuptools.setup(
    name='npm-register-cli',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/npm-register']
)
