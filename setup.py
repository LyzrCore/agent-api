from setuptools import setup, find_packages

setup(
    name="lyzr-agent-api",
    version="0.0.1",
    packages=find_packages(include=["lyzr_agent_api", "lyzr_agent_api.*"]),
    install_requires=[
        "httpx==0.27.2",
    ],
    author="lyzr",
    description="Official client for Lyzr Agent API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LyzrCore/lyzr-agent",
    python_requires=">=3.8.1, <3.12.5",
)
