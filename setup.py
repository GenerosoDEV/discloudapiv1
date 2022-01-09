from setuptools import setup, find_packages


with open('README.md', 'r') as fp:
    long_desc = fp.read()


setup(name='discloud_api',
      version='1.0.0',
      license='MIT',
      description='Módulo Python feito para acessar as rotas da discloudbot.com',
      long_description=long_desc,
      long_description_content_type="text/markdown",
      author='GenerosoDEV',
      url='https://github.com/GenerosoDEV/discloudapi',
      keywords=['discloudapi'],
      packages=find_packages(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Programming Language :: Python :: 3.8",
          "License :: OSI Approved :: MIT License",
          "License :: OSI Approved :: Apache Software License"
      ]
      )
