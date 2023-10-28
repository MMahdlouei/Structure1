import setuptools

setuptools.setup(
    include_package_data=True,
    name='main',
    version='0.0.1',
    description='module for learning python packages and ...',
    url='https://github.com/MMahdlouei/Learning',
    author='M.Mahdlouei',
    author_email='mahdlooyi@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=[],
    long_description='Mahdlouei learning python module',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'hello-world-cli = run:run'
        ],
    },
)