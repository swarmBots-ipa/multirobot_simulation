from setuptools import setup
import os
from glob import glob

package_name = 'multirobot_navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ipa',
    maintainer_email='ragesh.ramachandran@ipa.fraunhofer.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'main_function = multirobot_navigation.main:main',
            'reset_robot_pose=multirobot_navigation.robot_reset_pose:main',
            'send_pallet_pose=multirobot_navigation.send_pallet_poses:main'
        ],
    },
)
