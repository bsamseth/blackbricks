from setuptools import setup
import sys
import os

from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent


def get_long_description():
    readme_md = CURRENT_DIR / "README.md"
    with open(readme_md) as ld_file:
        return ld_file.read()


setup(
    name="blackbricks",
    description="Black for Databricks notebooks",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="automation formatter black sql yapf autopep8 pyfmt gofmt rustfmt",
    author="Bendik Samseth",
    author_email="b.samseth@gmail.com",
    url="https://github.com/psf/black",
    license="MIT",
    py_modules=["black", "blackd", "_black_version"],
    ext_modules=ext_modules,
    packages=["blib2to3", "blib2to3.pgen2"],
    package_data={"blib2to3": ["*.txt"]},
    python_requires=">=3.6",
    zip_safe=False,
    install_requires=[
        "click>=6.5",
        "attrs>=18.1.0",
        "appdirs",
        "toml>=0.9.4",
        "typed-ast>=1.4.0",
        "regex>=2020.1.8",
        "pathspec>=0.6, <1",
        "dataclasses>=0.6; python_version < '3.7'",
        "typing_extensions>=3.7.4",
        "mypy_extensions>=0.4.3",
    ],
    extras_require={"d": ["aiohttp>=3.3.2", "aiohttp-cors"]},
    test_suite="tests.test_black",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    entry_points={
        "console_scripts": [
            "black=black:patched_main",
            "blackd=blackd:patched_main [d]",
        ]
    },
)