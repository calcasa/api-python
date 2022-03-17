"""
    Copyright 2021 Calcasa B.V.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Calcasa Public API v1

    The version of the OpenAPI document: 1.1.2
    Contact: info@calcasa.nl
    Generated by: https://openapi-generator.tech
"""

from setuptools import setup, find_namespace_packages  # noqa: H301

NAME = "calcasa-api"
VERSION = "1.1.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    description="Calcasa Public API v1",
    author="Calcasa B.V.",
    author_email="info@calcasa.nl",
    url="https://github.com/calcasa/api-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Calcasa Public API v1"],
    classifiers=["Programming Language :: Python :: 3 :: Only", "License :: OSI Approved :: Apache Software License"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_namespace_packages(include=['calcasa.*'],exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache-2.0",
    long_description=long_description,
    long_description_content_type='text/markdown; charset=UTF-8; variant=GFM'
)
