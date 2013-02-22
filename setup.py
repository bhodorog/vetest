from setuptools import setup, find_packages

setup(
    name="vetest",
    version="0.0.1",
    description=("""Add vetest extension command to setuptools. Builds
an ve, pip installs test_requires packages, and launches tests_suite"""),
    author='Bogdan Hodorog',
    author_email='bogdan.hodorog@gmail.com',
    url="http://to.be.filled.in",
    license='BSD',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "distutils.commands": ["vetest = vetest:RunTests",]
    }
)