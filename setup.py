import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="video-konverter-SyntaxualSugar",
    version="0.0.1",
    author="Trenton Fox",
    author_email="tcfox54@gmail.com",
    description="Convert video files using ffmpeg.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SyntaxualSugar/VideoKonverter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console"
    ],
    python_requires='>=3.6',
)

