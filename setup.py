from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="codevault-cli",
    version="3.0.0",
    author="Dhruv",
    description="A terminal-based code explorer — browse, view, and run code in 10+ languages with live system monitoring",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["cli", "system_monitor"],
    python_requires=">=3.8",
    install_requires=[
        "psutil>=5.9.0",
    ],
    entry_points={
        "console_scripts": [
            "codevault=cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
)
