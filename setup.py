import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="myBlockChain", # Replace with your own username
    version="1.0.0",
    author="yathartharora",
    author_email="yathartharora1999@gmail.com",
    description="Create your own Blockchain",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yathartharora/blockChain",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
