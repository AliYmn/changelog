import sys

from setuptools import setup

if sys.version_info[0] < 3:
    with open('README.md') as f:
        README = f.read()
else:
    with open('README.md', encoding='utf-8') as f:
        README = f.read()

setup(
    name="changelogs-cli",
    version="1.0.0",
    author="Ali Yaman",
    author_email="aliymn.db@gmail.com",
    description="Generates git changelog for Conventional Commits",
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=README,
    keywords="Generates git changelog for Conventional Commits",
    packages=['changelog'],
    url='https://github.com/AliYmn/changelog',
    download_url='https://github.com/AliYmn/changelog',
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    entry_points={'console_scripts': ['changelog=changelog.src:main']},
)
