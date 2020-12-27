from distutils.core import setup
from setuptools import find_packages


NAME = 'softlearning'
VERSION = '0.0.1'
DESCRIPTION = (
    "Softlearning is a deep reinforcement learning toolbox for training"
    " maximum entropy policies in continuous domains.")


setup(
    name=NAME,
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    version=VERSION,
    description=DESCRIPTION,
    long_description=open('./README.md').read(),
    author='Kristian Hartikainen',
    author_email='kristian.hartikainen@gmail.com',
    url='https://github.com/rail-berkeley/softlearning',
    keywords=(
        'softlearning',
        'soft-actor-critic',
        'sac',
        'soft-q-learning',
        'sql',
        'machine-learning',
        'reinforcement-learning',
        'deep-learning',
        'robotics',
        'tensorflow',
        'tensorflow-2',
    ),
    entry_points={
        'console_scripts': (
            'softlearning=softlearning.scripts.console_scripts:main',
        ),
    },
    install_requires=(
        'Click>=7.0',
        'GitPython==3.1.2',
        'dm-control>=0.0.300771433',
        'gtimer>=1.0.0b5',
        'gym>=0.17.2',
        'mujoco-py>=2.0.2.10',
        'numpy>=1.17.5',
        'pandas',
        'ray[tune]>=0.8.0',
        'scikit-image>=0.17.2',
        'scikit-video>=1.1.11',
        'scipy>=1.4.1',
        'tensorflow>=2.2.0',
        'tensorflow-probability>=0.10.0',
        f'metaworld @ https://git@api.github.com/repos/rlworkgroup/metaworld/tarball/206b0263409147aa7aa572d501f74baa0c04c34b'
    ),
    zip_safe=True,
    license='MIT'
)
