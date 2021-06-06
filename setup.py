from setuptools import find_packages, setup

INSTALL_REQUIRES = ['opencv-python == 4.5.2.52',
                    'imutils == 0.5.4']

setup(
    name='mediafier',
    packages=find_packages(),
    version='0.1.0',
    description='Python library that helps with media (image/video) transformation and augmentation for machine learning and artificial vision projects. Enables the user to modify media for different purposes, as increasing a dataset or just changing some properties.',
    license='MIT',
    install_requires= INSTALL_REQUIRES,
    setup_requires=['pytest-runner==4.4'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',

    author = 'JParzival',
    author_email = 'jorge.deandres@hotmail.es',
    url = 'https://github.com/JParzival/mediafier',

    keywords = ['IMAGE', 'VIDEO', 'MEDIA', 'TRANSFORMATION', 'AUGMENTATION'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
  ]
)