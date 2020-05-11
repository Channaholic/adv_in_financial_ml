import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='PDS_Project',
    version='0.0.1dev1',
    description="Algo for price prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="",
    author_email="tomcelig@gmail.com",
    url="",
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'scikit-learn', 'click'],
    entry_points={
    }
)
