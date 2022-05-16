from setuptools import find_packages, setup

setup(
    name="dstack",
    version="0.1.1",
    description="A cli tool to manage your local stack",
    author="CSalih (Salih Candir)",
    url="https://github.com/CSalih/dstack",
    license="MIT License",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        "console_scripts": [
            "dstack = dstack.command:main",
        ]
    },
    python_requires=">=3.8",
    install_requires=[
        "click==8.1.3",
        "docker==5.0.3",
    ],
    extras_require={
        "dev": [
            "flake8==4.0.1",
            "black==22.3.0",
            "pylint==2.13.9",
            "pre-commit==2.19.0",
        ],
    },
)
