import setuptools
from glob import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="faciem",
    version="0.0.1",
    author="Deepak Raj",
    author_email="deepak008@live.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Py-Contributors/faciem",
    data_files=[('assets', glob('sanatio/assets/*'))],
    keywords="audiobook",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    project_urls={"Documentation": "https://pycontributors.readthedocs.io/projects/faciem/en/latest/",
                  "Source": "https://github.com/Py-Contributors/faciem",
                  "Tracker": "https://github.com/Py-Contributors/faciem/issues"},
    classifiers=["Development Status :: 2 - Pre-Alpha",
                 "Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Intended Audience :: Developers"],
    python_requires=">=3.4",
    include_package_data=True,
)
