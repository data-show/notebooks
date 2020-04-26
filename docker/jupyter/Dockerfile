FROM jupyter/minimal-notebook

COPY requirements.txt postBuild /tmp/

USER root

RUN apt-get update \
    && apt-get install -y \
        fonts-liberation \
        xvfb \
        libgtk2.0-0 \
        libgconf-2-4 \
        libxtst6 \
        libxss1 \
        i965-va-driver \
        libexpat1 \
        libgl1-mesa-dri \
        libglib2.0-0 \
        libgomp1 \
        libharfbuzz0b \
        libv4l-0 \
        libx11-6 \
        libxcb1 \
        libxext6 \
        libxml2 \
        ffmpeg \
        imagemagick \
        ghostscript \
    && conda install -c plotly --yes --file /tmp/requirements.txt \
    && conda clean --all -f -y \
    && npm cache clean --force \
    && rm -rf /var/lib/apt/lists/* && apt-get clean \
    && fix-permissions $CONDA_DIR \
    && fix-permissions /home/$NB_USER

# TODO: replace with postBuild script
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-leaflet && \
    npm cache clean --force

USER $NB_USER
