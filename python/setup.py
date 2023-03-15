from setuptools import setup, find_packages
setup(
    name="neuralforge",
    version="0.9.0",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=["numpy>=1.21.0", "typing-extensions>=4.0"],
)
