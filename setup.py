from setuptools import find_packages, setup

setup(
    name="MCQGENERATOR",
    version="0.0.1",
    author="Sreenivas Gurram",
    author_email="sreenivas.ai21@bmsce.ac.in",
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)