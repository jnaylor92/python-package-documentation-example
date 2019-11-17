from setuptools import setup, find_packages

EXTRAS = {'test': ['pytest', 'mock'],
          'docs': ['sphinx==1.7.5', 'sphinx_rtd_theme']}

setup(
    name='my_docs',
    version='0.0.1',
    author='',
    packages=find_packages(),
    install_requires=[],
    extras_require=EXTRAS,
    entry_points={
        'console_scripts': [],
    }
)
