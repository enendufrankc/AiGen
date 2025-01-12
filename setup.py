from setuptools import setup, find_packages

setup(
<<<<<<< HEAD
    name='aigent-lib',
=======
    name='aigen',
>>>>>>> 321da561b23bd63b26ce2a1f5955630d74dad073
    version='0.1.0',
    author='Frank Enendu',
    author_email='frank@favai.onmicrosoft.com',
    description='An open-source project designed to streamline the process of developing AI applications',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://https://github.com/enendufrankc/AiGen',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
<<<<<<< HEAD
    'console_scripts': [
        'aigent = aigent_lib.cli:cli'
    ],
=======
        'console_scripts': [
            'ai-template=aigen.cli:main',
        ],
>>>>>>> 321da561b23bd63b26ce2a1f5955630d74dad073
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
<<<<<<< HEAD
    python_requires='>=3.11',
=======
    python_requires='>=3.8',
>>>>>>> 321da561b23bd63b26ce2a1f5955630d74dad073
)
