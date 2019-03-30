import sys, os
from setuptools import setup, Extension

os.system("rm -r /Users/dguittet/SAM-Dev/PySAM/build")

libs = []
libpath = os.path.dirname(os.path.abspath(__file__))+"/lib"
libfiles = []
extra_link_args = ['-Wl,-rpath,'+'@loader_path/']
if sys.platform == 'darwin':
    from distutils import sysconfig
    vars = sysconfig.get_config_vars()
    vars['LDSHARED'] = vars['LDSHARED'].replace('-bundle', '-dynamiclib')
    libs = ['SAM_apid', 'sscd']
    libfiles = ['libSAM_apid.so', 'libsscd.so']

if sys.platform == 'linux':
    libs = ['SAM_apid', 'sscd']
    libfiles = ['libSAM_apid.so', 'libsscd.so']

if sys.platform == 'win32':
    libs = ['SAM_apid', 'sscd']
    libfiles = ['SAM_apid.dll', 'sscd.dll', 'SAM_apid.lib', 'sscd.lib']
    extra_link_args = ['']


setup(
    name='xx',
    version='1.3',
    include_package_data=True,
    packages=[''],
    package_dir={'': 'lib'},
    package_data={
        '': libfiles},
    ext_modules=[Extension('GenericSystem',
                           ['GenericSystem.c'],
                           include_dirs=[libpath],
                           library_dirs=[libpath],
                           libraries=libs,
                           extra_link_args=extra_link_args
                           )]
    )

