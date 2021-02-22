import setuptools

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='jc.robinhood',
    version='2.0.0',
    description='Unofficial Robinhood API client library for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jaredrcleghorn/robinhood',
    author='Jared Cleghorn',
    author_email='jaredrcleghorn@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=[
        'requests',
    ],
    python_requires='>=3.9',
)
