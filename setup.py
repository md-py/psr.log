import setuptools


with open('readme.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='psr.log',
    version='2.0.0',
    description='Common interface for logging libraries',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='License :: OSI Approved :: MIT License',
    package_dir={'psr': 'lib/psr'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    py_modules=['psr.log'],
    python_requires='>=3.6',
)
