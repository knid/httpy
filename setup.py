import sys

from setuptools import find_packages, setup

import httpy

tests_require = [
    "pytest",
]
dev_require = [
    *tests_require,
    "flake8",
    "pyyaml",
    "twine",
    "wheel",
]
install_requires = [
    "requests>=2.27.0",
    "Pygments>=2.5.2",
    "setuptools",
]

install_requires_win_only = [
    "colorama>=0.4.4",
]

if "bdist_wheel" not in sys.argv:

    if "win32" in str(sys.platform).lower():
        # Terminal colors for Windows
        install_requires.extend(install_requires_win_only)

extras_require = {
    "dev": dev_require,
    "test": tests_require,
    # https://wheel.readthedocs.io/en/latest/#defining-conditional-dependencies
    ':sys_platform == "win32"': install_requires_win_only,
}


def long_description():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


setup(
    name="httpy-cli",
    version=httpy.__version__,
    description="Modern, user-friendly, programmable command-line HTTP client for the API.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    author=httpy.__author__,
    author_email="sinan_kanidagli@hotmail.com",
    license=httpy.__licence__,
    packages=find_packages(include=["httpy", "httpy.*"]),
    entry_points={
        "console_scripts": [
            "httpy = httpy.__main__:main",
        ],
    },
    download_url="https://github.com/SinanKanidagli/httpy/archive/refs/tags/httpy-0.0.1.tar.gz",
    python_requires=">=3.7",
    extras_require=extras_require,
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development",
        "Topic :: System :: Networking",
        "Topic :: Terminals",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
    project_urls={
        "GitHub": "https://github.com/SinanKanidagli/httpy",
        "Twitter": "https://twitter.com/KanidagliV",
        "Documentation": "https://github.com/SinanKanidagli/httpy/docs",
    },
)
