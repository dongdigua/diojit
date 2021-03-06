from setuptools import setup, find_packages
from datetime import datetime
from pathlib import Path


version = "0.2a"
with Path("README.md").open() as readme:
    readme = readme.read()


setup(
    name="diojit",
    version=version if isinstance(version, str) else str(version),
    keywords="Just-In-Time, JIT, compiler",  # keywords of your project that separated by comma ","
    description="A general-purpose JIT for CPython.",  # a concise introduction of your project
    long_description=readme,
    long_description_content_type="text/markdown",
    license="mit",
    python_requires=">=3.8.0",
    url="https://github.com/thautwarm/diojit",
    author="thautwarm",
    author_email="twshere@outlook.com",
    packages=find_packages(),
    entry_points={"console_scripts": []},
    # above option specifies what commands to install,
    # e.g: entry_points={"console_scripts": ["yapypy=yapypy.cmd:compiler"]}
    install_requires=["pyrsistent", "julia"],  # dependencies
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)
