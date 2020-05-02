from setuptools import setup, find_packages

setup(name='myturtle',
      version='0.1',
      description='Simple turtle implementation.',
      long_description='Implementation of turtle based on matplotlib and working in Jupyter Notebooks.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Education',
      ],
      keywords='turtle jupyter notebook',
      author='Martin Claus',
      author_email='mclaus@geomar.de',
      url='https://github.com/martinclaus/myturtle',
      license='MIT',
      packages=find_packages(),
      install_requires=[
        'numpy',
        'matplotlib',
      ],
)
