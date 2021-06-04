import re
from setuptools import find_packages, setup 

INSTALL_REQUIRES = ["opencv-python", "numpy", "matplotlib", "scikit-image"]

TEST_REQUIRES = [
    "pytest<5.4.0",
    "pytest-cov==2.8.1",
    "pytest-sugar==0.9.2",
    "black",
    "pre-commit",
    "flake8",
    "mypy",
    "bandit",
]

setup(
    name="picture_evo",
    version="0.1",
    description="진화 알고리즘으로 김준영의 얼굴을 그려보자!",
    url="https://github.com/hjg0706/picture_evo",
    packages=find_packages(),
    download_url="",
    author="Hong Jungi",
    python_requires=">=3.6",
    setup_requires=["wheel"],
    install_requires=INSTALL_REQUIRES,
    extras_require={"test": TEST_REQUIRES},
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
)
