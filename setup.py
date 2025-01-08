from setuptools import setup, find_packages

setup(
    name="gdocs-automation",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "google-auth-oauthlib>=0.4.6",
        "google-auth-httplib2>=0.1.0",
        "google-api-python-client>=2.0.0",
        "jinja2>=3.0.0",
        "pyyaml>=5.4.1",
    ],
    python_requires=">=3.8",
    author="Your Name",
    author_email="your.email@example.com",
    description="An advanced system for automating Google Docs operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/gdocs-automation",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
) 