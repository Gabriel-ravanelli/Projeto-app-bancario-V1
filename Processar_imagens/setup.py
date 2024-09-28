from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Processar_imagens",
    version="0.0.1",
    author="Gabriel ravanelli genaro da silva",
    author_email="@@email",
    description="Pacote inicial para estudo",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gabriel-ravanelli/Projeto-app-bancario-V1/blob/main/Processar_imagens/setup.py",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
