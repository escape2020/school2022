FROM continuumio/miniconda3:4.12.0

COPY . /home/school2022
WORKDIR /home/school2022

RUN conda install mamba -n base -c conda-forge && \
    mamba env create -f environment.yml

ENV PATH /opt/conda/envs/$conda_env/bin:$PATH
ENV CONDA_DEFAULT_ENV eschool2022

RUN echo "conda activate eschool2022" >> ~/.bashrc

CMD bash

