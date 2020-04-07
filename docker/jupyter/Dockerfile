FROM jupyter/minimal-notebook

COPY requirements.txt postBuild ./

RUN pip install --no-cache-dir -r requirements.txt

# TODO: replace with postBuild script
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-leaflet
