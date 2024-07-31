#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from setuptools import setup


with open("README.md", "r") as f:
    readme = f.read()

version = ""
with open("framework/_version.py") as f:
    match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)
    if not match:
        raise RuntimeError("version is not set")

    version = match.group(1)

if not version:
    raise RuntimeError("version is not set")


extras = {
    "dev": [
        "twine>=3.4.1",
    ]
}

setup(
    name="dl-framework-generator",
    version=version,
    author="Sushrut Patwardhan",
    maintainer="Sushrut Patwardhan",
    license="MIT",
    url="https://github.com/Blazkowiz47/torch-framework-python",
    description="Deep learning project structure generator.",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=["framework"],
    python_requires=">=3.6",
    package_data={"": ["py.typed"]},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "framework=framework.cli:entrypoint",
            "framework-python=framework.cli:entrypoint",
        ],
    },
    extras_require={
        **extras,
        "all": [req for requirements in extras.values() for req in requirements],
    },
    project_urls={
        "Source": "https://github.com/Blazkowiz47/torch-framework-python",
        "Tracker": "https://github.com/Blazkowiz47/torch-framework-python/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Typing :: Typed",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
