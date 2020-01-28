
pyver, pyvers  = '>=3.7', (3,7)

import sys
if sys.version_info < pyvers:
    sys.exit('ERROR: require Python %s'%pyver)

get = {}
with open('src/hycpy/version.py') as f:
    exec(f.read(),get)


from setuptools import setup, find_packages
setup(
# -----------
name='hycpy',
description = "Henry's Python modules",
version = get['version'],
url = 'https://github.com/hyiprc/hycpy',
# -----------
author = 'Henry Chan',
author_email = 'hyiprc@gmail.com',
# -----------
python_requires=pyver,
install_require = ['numpy','scipy'],
packages = find_packages('src',exclude=('hycpy.template',)),
package_dir={'':'src'},
# -----------
#entry_points = {
#'console_scripts':[
#    'hycpy = hycpy.__main__:help',
#],
#'gui_scripts':[
#    # on Windows, no console window
#],
#},
# -----------
#test_suite='tests',
)

#from setuptools import Extension
#from Cython.Build import cythonize
# -----------
#ext_modules = cythonize([
#    "_dbscan_inner", sources=["clustering/_dbscan_inner.pyx"], 
#    include_dirs=[numpy.get_include()], 
#    extra_compile_args=["-O3"], language="c++"
#]),
