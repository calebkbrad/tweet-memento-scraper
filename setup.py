from setuptools import setup, find_packages

setup(
    name='tweet_memento_scraper',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
        'beautifulsoup4',
        'googletrans==3.1.0a0'
    ],
    entry_points={
        'console_scripts': [
            'test_script = tweet_memento_scraper.scripts.main:cli',
            'scrape_tweet_memento = tweet_memento_scraper.scripts.main:scrape_tweet_memento',
            'scrape_tweet_mementos = tweet_memento_scraper.scripts.main:scrape_tweet_mementos',
            'scrape_profile_memento = profile_memento_scraper.scripts.main:scrape_profile_memento',
            'scrape_profile_mementos = profile_memento_scraper.scripts.main:scrape_profile_mementos'
        ],
    },
)