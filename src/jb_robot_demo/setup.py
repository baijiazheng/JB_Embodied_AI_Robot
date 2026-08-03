from setuptools import find_packages, setup

package_name = 'jb_robot_demo'

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
    maintainer='jb',
    maintainer_email='3248428889@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        	'status_node = jb_robot_demo.status_node:main',
		'command_node = jb_robot_demo.command_node:main',
		'controller_node = jb_robot_demo.controller_node:main',
		'safety_node = jb_robot_demo.safety_node:main',
	],
    },
)
