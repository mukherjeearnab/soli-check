# SoliCheck

SoliCheck is a vulnerability detection model based on the [soli-swc](https://github.com/mukherjeearnab/soli-swc) project. It is built using the Django Web Framework, providing a web interface to submit Ethereum Smart Contract OPCODES, and obtain a vulnerability detection report. The model is built using Tensoflow, based on the LSTM architecture.

During the evaluation of the model, it achieved an F-1 score of 97.81%.

# Getting Started

To run the App locally, follow the steps below:

## Prerequisites

Before you can start with the installation, you need to install the Conda package manager. Follow this [link](https://docs.conda.io/en/latest/miniconda.html) to install it.

## Installation

First you need to create the conda environment for running the app. The `conda_env.yml` contains the configuration for the environment. Run:

    conda env create -f ./conda_env.yml

Once, the environment is created, activate the environment using:

    conda activate django_env

## Execution

To run the Django Web App, run the following command inside the repository directory:

    python manage.py runserver
