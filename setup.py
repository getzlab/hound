from setuptools import setup

version_ns = {}
with open('hound/_version.py') as v:
    exec(v.read(), version_ns)
__version__ = version_ns['__version__']

with open('README.md') as r:
    long_description = r.read()

setup(
    name = 'hound',
    version = __version__,
    packages = [
        'hound',
    ],
    description = 'A FireCloud database extension',
    url = 'https://github.com/getzlab/hound',
    author = 'Aaron Graubert - Broad Institute - Cancer Genome Computational Analysis - Getz Lab',
    author_email = 'aarong@broadinstitute.org',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    python_requires = ">=3.14, <3.15",
    install_requires = [
        "google-cloud-storage>=3.7.0",
        "google-auth>=2.0.0",
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
    ],
    license="BSD3"
)
