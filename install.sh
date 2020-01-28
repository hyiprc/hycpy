#!/usr/bin/env bash

py=$(which pip 2>/dev/null)
if [ $? -ne 0 ];then
    printf "\\nERROR: cannot find python pip, aborting installation\\n"
    exit 2
fi

printf "\\nInstall HycPy via\\n$py\\n"
printf "Proceed (y|[n])? >>> ";read -r ans
if [ "$ans" != "y" ];then
    printf "aborting installation\\n"
    exit 2
fi

printf ">>> conda install pip numpy scipy\\n"
conda install pip numpy scipy

{
#pip install .
printf ">>> pip install -e .\\n"
pip install -e .
# --- alternatives ---
#python setup.py install
#python setup.py develop
} || {
printf "\\nFall-back, adding path to .egg-link and easy-install.pth in\\n"
site=$(python -c "import site; print(site.getsitepackages()[0])")
printf "$site\\n"
srcdir="$(pwd)/src"
echo $srcdir > $site/hycpy.egg-link
echo $srcdir >> $site/easy-install.pth
}
