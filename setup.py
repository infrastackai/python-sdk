#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()
setup(
    name="infrastack",
    version="0.0.0",
    description="""Empowering Developers with AI-First DevTools""",
    long_description="".join(open("README.md", encoding="utf-8").readlines()),
    long_description_content_type="text/markdown",
    url="https://github.com/infrastackai/python-sdk",
    author="Infrastack AI",
    author_email="info@infrastack.ai",
    license="MIT",
    packages=["infrastack"],
    install_requires=install_requires,
    python_requires=">= 3",
    zip_safe=False,
)



