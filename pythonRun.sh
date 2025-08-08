# Name environment
ENV_NAME=visualisation
ACTIVATE=${PWD}/${ENV_NAME}/bin/activate
KERNEL_PATH=~/.local/share/jupyter/kernels/

# Install packages if this is fresh start
if [[ ! -e "${ACTIVATE}" ]]; then

    # note --system-site-packages to get ROOT from base install
    python3 -m venv --system-site-packages ${ENV_NAME}
    source ${ACTIVATE}

    pip3 install --upgrade pip
    pip3 install nibabel
    pip3 install open3d
    pip3 install uproot
    pip3 install matplotlib

    # This part adds the venv to Jupyter
    #if [[ ! -e "${KERNEL_PATH}/${ENV_NAME}" ]]; then
    #    pip3 install ipykernel
    #    python3 -m ipykernel install --user --name=${ENV_NAME}
    #else
    #    echo "Kernel named ${ENV_NAME} already exists in ${KERNEL_PATH}"
    #fi
else
    source ${ACTIVATE}
fi

