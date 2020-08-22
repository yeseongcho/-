from setuptools import setup, find_packages

setup_requires = [
    ]

install_requires = [
    'pillow==3.4.2'
    ]

dependency_links = [
    ]

setup(
    name='sit22001',
    version='0.2.3',
    description='course materials for SIT22001',
    author='cbchoi',
    author_email='cbchoi@handong.edu',
#    packages=["SIT22001"],
    py_modules= ['cs1graphics', 'cs1media', 'cs1robots', 'cs1robots_images', 'easygui'],
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    # scripts=['manage.py'],
    entry_points={
        'console_scripts': [
            ],
#        "egg_info.writers": [
#                "foo_bar.txt = setuptools.command.egg_info:write_arg",
#            ],
        },
    )
