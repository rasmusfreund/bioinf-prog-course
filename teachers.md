

# For teachers of the course

## Conda environment

To create the `bp2020` conda environment with the libraries required to run evaluation of exam assignments you create it like this:

	conda create -c conda-forge -c farrajota --name bp2020 jupyter jupyterlab matplotlib seaborn pandas numpy pyyaml scipy yaml pypdf2 patool jupyterlab pandoc pandoc-crossref cryptography pandoc pandoc-crossref

To compile files for the exam, you also need MacTeX installed