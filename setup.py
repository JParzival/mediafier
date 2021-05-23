from setuptools import find_packages, setup

setup(
    name='python_lib_name',
    packages=find_packages(include=['python_lib_name']),
    version='0.1.0',
    description='My Python library',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',

    author = 'YOUR NAME',
    author_email = 'your.email@domain.com',
    url = 'https://github.com/user/reponame',

    keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
  ]
)