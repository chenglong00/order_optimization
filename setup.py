from setuptools import setup, find_packages

setup(name='order-optimizer',
      version='1.0.0',
      description="Spaceship Order Optimizer",
      long_description="""
      Order Optimizer: an external api to calculate the maximum profit from a list of contracts
      """,
      packages=find_packages(exclude="tests"),
      install_requires=[
          'uvicorn>=0.21.1',
          'fastapi>=0.95.0',
          'pydantic>=1.10.2'
      ],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      keywords='spaceship,order,optimizer',
      author='Wu Chenglong',
      author_email='chenglong.w1@gmail.com',
      license='MIT')
