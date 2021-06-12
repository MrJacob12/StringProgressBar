from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='StringProgressBar',
  version='1.0.1',
  description='Simple string progress bar made for discord bots. Its usable everywhere.',
  long_description= open('README.md', encoding="utf8").read() + '\n\n' + open('CHANGELOG.txt', encoding="utf8").read(),
  long_description_content_type='text/markdown',
  url='https://github.com/MrJacob12/TextProgressBar',  
  author='MrJacob',
  author_email='jacob@fern.fun',
  license='MIT', 
  classifiers=classifiers,
  keywords='String Progress Bar', 
  packages=find_packages(),
  install_requires=[''] 
)
