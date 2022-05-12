# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="clearcut",
    version="0.2.0",
    description="A straightforward and lightweight logging wrapper library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tangibleintelligence/clearcut",
    author="Tangible Intelligence",
    author_email="austin@tangibleintelligence.com",
    classifiers=[  # Optional
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="logging",
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    # TODO otlp deps, or maybe poetry
)
