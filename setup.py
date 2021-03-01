import setuptools

setuptools.setup(
    name="pyintersection-Flodri", # Replace with your own username
    version="0.1.0",
    author="Flodri",
    #author_email="author@example.com",
    description="A lightweight pure python library which implement a couple of geometric primitives and their intersection functions.",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    url="https://github.com/flodri/pyintersection",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.4',
)
