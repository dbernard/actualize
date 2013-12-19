from setuptools import setup, find_packages
from actualize import version as VERSION

setup(
        name = "actualize",
        version = VERSION,
        packages = find_packages(exclude=['.*tests*']),
        entry_points = {
            'console_scripts': [
                'actualize = actualize.cli:main'
            ]
        },
        author = 'DB',
        author_email = 'abc@xyz.net',
        description = 'Makes creating new projects easy.',
        long_description = 'Long description here.',
        license = "BSD")
