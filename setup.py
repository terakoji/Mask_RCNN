from setuptools import setup, find_packages

setup(
    name='mask_rcnn',
    version='2.0.0',
    description='Mask R-CNN for Object Detection and Segmentation',
    long_description='README.md',
    author='Waleed Abdulla',
    author_email='waleed.abdulla@gmail.com',
    install_requires=['scikit-image',
                      'docopt',
                      'clint',
                      'tablib',
                      'cython',
                      'keras'],
    dependency_links=['git+https://github.com/pdollar/coco.git#egg=pycocotools&subdirectory=PythonAPI'],
    url='https://github.com/matterport/Mask_RCNN',
    license='MIT',
    packages=find_packages(exclude=('images', 'assets'))
)
