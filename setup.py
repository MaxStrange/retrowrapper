__doc__ = """Wrapper for OpenAI Retro Gym to allow multiple processes."""

from setuptools import setup

setup(
    name="retrowrapper",
    version="0.2.0",
    author="Max Strange",
    author_email="maxfieldstrange@gmail.com",
    description="Wrapper for OpenAI Retro Gym environments to allow multiple processes.",
    install_requires=["gym-retro"],
    license="MIT",
    keywords="reinforcement-learning retro ai rl dl deep-learning gym openai",
    url="https://github.com/MaxStrange/retrowrapper",
    py_modules=["retrowrapper"],
    python_requires="~=3.4",
    long_description=__doc__,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)