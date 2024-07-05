from setuptools import setup

setup(
    name='dyca',
    version='0.1.0',
    description='Dynamical Component Analysis - A method to decompose multivariate signals',
    author='Annika Stiehl',
    author_email='annika.stiehl@hs-ansbach.de',
    license='GPL-3.0',
    packages=['dyca'],
    install_requires=['numpy==1.26.4', 'matplotlib==3.8.4', 'scipy==1.13.0'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Signal Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Signal Decomposition',
    ],

)
