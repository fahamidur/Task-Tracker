from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="task_tracker",
    version="0.1",
    author="Fahamidur Rahaman Rafi",
    author_email="fahamidur2000@gmail.com",
    description="A CLI tool for tracking tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/task_tracker",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas>=1.0.0',  # For data manipulation and reporting
        'openpyxl>=3.0.7',  # For Excel report generation
        'python-dateutil>=2.8.1',  # For date parsing and manipulation
        # Add more dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'task-tracker=task_tracker.__main__:main',
        ],
    },
)
