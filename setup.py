from setuptools import setup  # type: ignore

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pydantic-mermaid',
    version='0.3.0',
    description='Convert pydantic classes to markdown mermaid class charts',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Eric Websmith',
    author_email='eric.websmith@gmail.com',
    url='https://github.com/EricWebsmith/pydantic_mermaid',
    packages=['pydantic_mermaid'],
    package_data={'pydantic_mermaid': ['py.typed']},
    install_requires=[
        'pydantic'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'pydantic-mermaid = pydantic_mermaid.__main__:main'
        ]
    }
)
