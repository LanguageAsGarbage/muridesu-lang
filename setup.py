from setuptools import setup, find_packages
from datetime import datetime
from devpackage.disttools.version import Version
from devpackage.disttools.path import Path

with open(".meta_version", "r") as meta_version:
    meta_version_config = dict(each.strip().split(":")
                               for each in meta_version.read().splitlines())
version_method = meta_version_config.get("method")

if version_method is None:
    version = '0.0.1'
elif version_method.strip() == "timeversion":
    version = datetime.today().timestamp()
elif version_method.strip() == "autoinc":
    version = Version(meta_version_config["current"].strip())
else:
    raise Exception("Invalid `version_method`. Check your .meta_version.")

with Path('README.md').open() as readme:
    readme = readme.read()

setup(
    name='muridesu',
    version=version if isinstance(version, str) else str(version),
    keywords="",  # keywords of your project that separated by comma ","
    description="",  # a conceise introduction of your project
    long_description=readme,
    long_description_content_type="text/markdown",
    license='mit',
    python_requires='>=3.6.0',
    url='https://github.com/thautawarm/muridesu',
    author='thautawarm',
    author_email='twshere@outlook.com',
    packages=find_packages(),
    entry_points={"console_scripts": ["muridesu=muridesu.cli:main"]},
    # above option specifies commands to be installed,
    # e.g: entry_points={"console_scripts": ["yapypy=yapypy.cmd.compiler"]}
    install_requires=["devpackage", 'argser', 'rbnf-rts', 'remu-operator'],
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)

if isinstance(version, Version):
    meta_version = Path(".meta_version").open("w")
    version.increment(2, 1)
    for i in range(2, 0, -1):
        version.carry_over(i, 42)
    meta_version.write("method: autoinc\n")
    meta_version.write(f"current: {version}")
