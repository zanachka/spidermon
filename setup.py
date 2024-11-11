from setuptools import find_packages, setup

setup(
    name="spidermon",
    version="1.23.0",
    url="https://github.com/scrapinghub/spidermon",
    project_urls={
        "Documentation": "https://spidermon.readthedocs.io/",
        "Source": "https://github.com/scrapinghub/spidermon",
        "Tracker": "https://github.com/scrapinghub/spidermon/issues",
        "Release notes": "https://spidermon.readthedocs.io/en/latest/changelog.html",
    },
    author="Zyte",
    author_email="opensource@zyte.com",
    description=("Spidermon is a framework to build monitors for Scrapy spiders."),
    long_description=open("README.rst", encoding="utf-8").read(),
    license="BSD",
    packages=find_packages(),
    package_data={"spidermon": ["VERSION"]},
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "jsonschema[format]>=4.21.0",
        "python-slugify",
    ],
    extras_require={
        # Specific monitors and tools to support notifications and reports
        "monitoring": [
            "Jinja2",
            "boto",
            "boto3",
            "itemadapter",
            "premailer",
            "requests",
            "scrapinghub",
            "scrapinghub-entrypoint-scrapy",
            "scrapy",
            "sentry_sdk",
            "slack_sdk",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Scrapy",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: System :: Monitoring",
    ],
    python_requires=">=3.8",
)
