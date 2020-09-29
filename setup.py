import setuptools

with open("README", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emvframework",
    version="0.0.1",
    author="Dorian Peake",
    author_email="dorian@vereia.com",
    description="EMV Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dozzman/emv-framework",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pyscard>=2.0.0',
        'lxml==4.5.2'
    ],
    python_requires='>=3.6',
)


