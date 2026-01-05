"""
YouTube Video İndirici - Setup Script
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="yt-downloader",
    version="1.0.0",
    author="İhsan Bakı Doğan",
    author_email="contact@ihsanbakidogan.com",
    description="Python ile yazılmış kullanımı kolay YouTube video indirme aracı",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ibidi/yt-download",
    project_urls={
        "Bug Tracker": "https://github.com/ibidi/yt-download/issues",
        "Documentation": "https://github.com/ibidi/yt-download#readme",
        "Source Code": "https://github.com/ibidi/yt-download",
        "Website": "https://ihsanbakidogan.com",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Video",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    py_modules=["youtube_downloader"],
    python_requires=">=3.8",
    install_requires=[
        "yt-dlp>=2023.12.30",
    ],
    entry_points={
        "console_scripts": [
            "yt-downloader=youtube_downloader:main",
        ],
    },
    keywords="youtube downloader video audio mp3 yt-dlp",
)

