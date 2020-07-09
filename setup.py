import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dependency-fixer",
    version="1.0.1",
    author="Avinash Karhana",
    author_email="avinashkarhana1@gmail.com",
    description="A simple inscript multi-package installer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avinashkarhana/dependencyfixer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)