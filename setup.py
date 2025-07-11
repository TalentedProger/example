from setuptools import setup, find_packages

setup(
    name="my_simple_bot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "aiogram==3.20.0.post0",
        "aiohttp==3.11.18",
        "python-dotenv==1.1.1",
    ],
    python_requires=">=3.11",
)
