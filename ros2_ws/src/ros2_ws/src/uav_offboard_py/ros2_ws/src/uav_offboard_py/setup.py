from setuptools import setup

package_name = 'uav_offboard_py'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jhonattan Jesus Ojeda Arroyo',
    maintainer_email='jhony.ojeda565@gmail.com',
    description='ROS 2 Jazzy PX4 offboard control node for UAV environmental monitoring missions.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'offboard_mission = uav_offboard_py.offboard_mission:main',
        ],
    },
)

