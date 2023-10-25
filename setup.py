from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='WebifyPy',
    version='0.1.0',
    author='Ishan Oshada',
    author_email='ic31908@gmail.com',
    description='A Python package for web development',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ishanoshada/WebifyPy',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/ishanoshada/WebifyPy/issues',
        'Source': 'https://github.com/ishan oshada/WebifyPy',
    },
    keywords='web development, Python package ',
    license='MIT',
)
