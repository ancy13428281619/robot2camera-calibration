from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

def license():
    with open('license.rst') as f:
        return f.read()

setup(name='robot2cam_calibration',
      version='0.1',
      description='A package to calibrate a UR CB2 Robot to a camera',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='universal robots cb2 ur5 flycapture2 point grey',
      url='-',
      author='Michael Sobrepera',
      author_email='mjsobrep@live.com',
      license=license(),
      packages=['robot2cam_calibration'],
      install_requires=[
          'numpy',
          'cv2',
          'flycapture2',
          'ur_cb2'
      ],
      include_package_data=True,
      entry_points={
        'console_scripts': ['robot2cam-record=ur_cb2.receive.cb2_receive_example:'
                            'main',
                            'robot2cam-calculate=ur_cb2.receive.cb2_store_points:main',
                            'robot2cam-show=']
      },
      zip_safe=False)
