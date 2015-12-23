CAS Categorization
====

CAS Categorization is a playground the test the categorizing CAS Activities. Because of the limitations of Heroku, this application will be employing [Conda](http://conda.pydata.org/docs/) to manage our libraries.

## System Requirements:
- Python 3
- (coming soon) PostgreSQL

## Local Setup:
1. Ensure that Python 3 is installed on your local machine.
2. Install Miniconda with the instructions [here](http://conda.pydata.org/docs/install/quick.html).
3. Set up a new Conda environment with pip as the first package to be installed:
`conda create -n cas pip`
4. Activate Conda environment: `source activate cas`
5. Update pip: `pip install -U pip`
6. Install SciPy: `conda install scipy`
7. Install the pip requirements: `pip install -r requirements.txt`

### TODO:
- Setup script for Conda setup

**Requirement file notes:** Scipy cannot be installed via pip because of its required dependencies (BLAS/Lapack).
