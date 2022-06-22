FROM jupyter/datascience-notebook:python-3.10.4

USER root

COPY . /home/jovyan/school2022
WORKDIR /home/jovyan/school2022


RUN conda install mamba -n base -c conda-forge
RUN  mamba env create -f environment.yml

ENV PATH /opt/conda/envs/$conda_env/bin:$PATH
ENV CONDA_DEFAULT_ENV eschool2022

RUN echo "conda activate eschool2022" >> ~/.bashrc

RUN conda clean --all

WORKDIR $HOME
USER $NB_USER

RUN rm -rf work/

