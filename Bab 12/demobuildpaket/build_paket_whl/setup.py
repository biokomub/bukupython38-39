import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ujikimiatanah-whl",
    version="0.1.0",
    author="Brian Rahardi",
    author_email="brian_rhardi@ub.ac.id",
    description="pustaka untuk menguji parameter kimia tanah",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://komputasi.biologi.ub.ac.id/",
    project_urls={
        "Bug Tracker": "https://komputasi.biologi.ub.ac.id/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
