from setuptools import setup, find_packages

setup(
    name='tweet_memento_scraper',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'test_script = tweet_memento_scraper.scripts.main:cli',
        ],
    },
)