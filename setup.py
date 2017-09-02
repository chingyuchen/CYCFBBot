'''
Create cycfbbot package
Copyright (c) 2017 Ching-Yu Chen
'''

setup(
        name="cycfbbot",
        version="1.0",
        author="Ching-Yu Chen",
        author_email="chingyuc.cyc@gmail.com",
        maintainer='Ching-Yu Chen',
        maintainer_email='chingyuc.cyc@gmail.com',
        packages=["cycfbbot"],
        license="LICENSE",
        description="A framework of a facebook bot",
        long_description=open("README.md").read(),
        install_requires=[
            'fbmq>=2.1.0',
            'Flask>=0.12.2',
            'pymessenger>=0.0.7.0',
        ],
        scripts=['cycfbbot'],
)

