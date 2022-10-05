# LogTransform
#### Omar Halawa (ohalawa@ucsd.edu) at the Mesirov Lab - University of California, San Diego
\
The following repository is a GenePattern module written in Python 3, using the following [Docker image](https://hub.docker.com/layers/genepattern/notebook-python39/21.08/images/sha256-12b175ff4472cfecef354ddea1d7811f2cbf0ae9f114ede11d789b74e08bbc03?context=explore). 

It takes in an input GCT file, process it by taking the natural log of each of its positive data points (turning all non-positive values into 0), and outputs a new GCT file of the processed data. Documentation on usage and implementation is found [here](https://github.com/omarhalawa3301/log_normalize/blob/main/docs/tutorial.md).

All source files, including a [sample test file](https://github.com/omarhalawa3301/log_normalize/blob/main/data/all_aml_train.gct) and [expected output file](https://github.com/omarhalawa3301/log_normalize/blob/main/data/result.gct), are available for better reproducibility and portability. 



