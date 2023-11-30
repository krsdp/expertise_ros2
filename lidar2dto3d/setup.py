from setuptools import find_packages, setup

package_name = 'lidar2dto3d'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kursad',
    maintainer_email='ak.polat@student.avans.nl',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            '3dlidar_node = lidar2dto3d.3dlidar:main',
            'publisher = lidar2dto3d.publisher:main',
            'subscriber = lidar2dto3d.subscriber:main',
        ],
    },
)
