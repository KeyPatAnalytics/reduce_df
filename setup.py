from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='reduce_df',
  version='0.0.1',
  description='optimize local memory usages',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Keyela Patatchona',
  author_email='patatchona@outlook.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='data nalysis, data frame, size reduction, less memory', 
  packages=find_packages(),
  install_requires=['numpy'] 
)