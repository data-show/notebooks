FROM jupyter/minimal-notebook

COPY requirements.txt postBuild ./

RUN pip install --no-cache-dir -r requirements.txt
RUN ./postBuild
