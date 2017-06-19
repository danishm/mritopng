from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='mritopng',
    version='0.1',
    description='Easily convert MRI filed based on the DICOM format to a PNG image',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Environment :: Console',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: End Users/Desktop'
    ],
    url='https://github.com/danishm/mritopng',
    author='Danish Mujeeb',
    author_email='danish@dsharpapps.com',
    license='MIT',
    packages=['mritopng'],
    zip_safe=False,
    install_requires=[
        'pypng',
        'pydicom'
    ],
    entry_points={
        'console_scripts': ['mritopng:mritopng.command_line:main'],
    }
)
