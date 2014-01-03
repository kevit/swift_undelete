#!/usr/bin/python
# Copyright (c) 2013 Samuel N. Merritt <sam@swiftstack.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

version = "0.0.1"

setup(
    name="swift_undelete",
    version=version,
    description='Undelete middleware for OpenStack Swift',
    license='Apache License (2.0)',
    author='Samuel N. Merritt',
    author_email='sam@swiftstack.com',
    url='https://github.com/swiftstack/swift-undelete',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Environment :: No Input/Output (Daemon)'],
    install_requires=[],
    test_suite='nose.collector',
    tests_require=["nose"],
    scripts=[],
    entry_points={
        'paste.filter_factory': ['undelete=swift_undelete:filter_factory']})
