import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyPolkaSideCar-mickstar", # Replace with your own username
    version="0.0.1",
    author="Michael Johnston",
    author_email="michael.johnston29@gmail.com",
    description="A Simple wrapper for the substrate sidecar for polkadot nodes",
    license="GPLv3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mickstar/PyPolkaSideCar",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        "requests"
    ],
    python_requires='>=3.6',
)
