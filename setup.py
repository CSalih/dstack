from setuptools import setup, find_packages

setup(
    name='dstack',
    version='0.1.1',
    description='A cli tool to manage your local stack',
    author='CSalih (Salih Candir)',
    url='https://github.com/CSalih/dstack',
    license='MIT License',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'Click',
    ],
    entry_points={
        "console_scripts": [
            "dstack = dstack.command:main",
        ]
    },
)
