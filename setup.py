import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parsley-beesperester",
    version="0.0.2",
    author="Bernhard Esperester",
    author_email="bernhard@esperester.de",
    description="Use simple recipes to extract, mutate and validate data from BeautifulSoup objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/beesperester/python-parsley",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)