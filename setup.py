from setuptools import find_packages, setup

INSTALL_REQUIRES = ['opencv-python == 4.5.2.52',
                    'imutils == 0.5.4']

setup(
    name='imgTransPy',
    packages=find_packages(include=['imgTransPy']),
    version='0.1.0',
    description='Python library made for doing Data Augmentation and Data Transformation over images in a simple way',
    license='MIT',
    install_requires= INSTALL_REQUIRES,
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',

    author = 'JParzival',
    author_email = 'jorge.deandres@hotmail.es',
    url = 'https://github.com/JParzival/imgTransPy',

    keywords = ['IMAGE', 'TRANSFORMATION', 'AUGMENTATION'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
  ]
)