from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pydantic_mermaid',
    version='0.1.0',
    description='Convert pydantic classes to markdown mermaid class charts',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Eric Websmith',
    author_email='eric.websmith@example.com',
    url='https://github.com/EricWebsmith/pydantic_mermaid',
    packages=['pydantic_mermaid'],
    package_data={'pydantic_mermaid': ['py.typed']},
    install_requires=[
        # List your dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
