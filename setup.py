import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name = 'google_api_v3_helper',
    version = '0.2.dev0',
    author="Renaud Viot",
    author_email="renaud.viot@simply-bi.com",
    description = 'help python developper to use some of the Google Drive API v3 easily',
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sbi-rviot/google_api_helper",
    install_requires = ['oauth2client', 'google-api-python-client==1.7.9', 'google-auth-httplib2==0.0.3','google-auth-oauthlib==0.4.0'],
    packages=['google_api_v3_helper'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    )

