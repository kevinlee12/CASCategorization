CAS Categorization
==================

CAS Categorization is a playground the test the categorizing CAS Activities.
Because of the limitations of Heroku, this application will be employing
[Conda](http://conda.pydata.org/docs/) to manage our libraries.

## System Requirements:
- Python 3
- (coming soon) PostgreSQL

## Local Setup:
1. Ensure that Python 3 is installed on your local machine.
2. Install Miniconda with the instructions
[here](http://conda.pydata.org/docs/install/quick.html).
3. Set up the Conda environment with the specified settings using
`conda env create -f environment.yml`.
    - If you have a Mac and run into issues at this stage, please completely
    remove `libgfortran=1.0=0` and `scipy=0.17.0=np110py35_1` from
    `environment.yml` and try again.
4. Activate Conda environment: `source activate cas`
    - If you had to omit those lines mentioned in 3, please
    manually reinstall the packages with the following commands:
    `conda install -n cas scipy`.
7. Install the pip requirements: `pip install -r requirements.txt`

### TODO:
- Setup script for Conda setup

**Requirement file notes:** Scipy cannot be installed via pip
because of its required dependencies (BLAS/Lapack). Therefore, it is not in
requirements.txt file.
