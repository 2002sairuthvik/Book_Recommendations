from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Book_Recommendations"
AUTHOR_USER_NAME = "Sai Ruthvik"
SRC_REPO = "books_recommendations"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Sai Ruthvik Munugoti",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/2002sairuthvik/Book_Recommendations",
    author_email="msairuthvik@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)