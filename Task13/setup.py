from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'traffic_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # Include launch files
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.py')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='omar-abdallah',
    maintainer_email='omar-abdallah@todo.todo',
    description='ROS 2 package for autonomous traffic manager',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'fleet_simulator = traffic_system.fleet_simulator:main',
            'traffic_manager = traffic_system.traffic_manager:main',
        ],
    },
)