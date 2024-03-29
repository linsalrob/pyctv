[![Edwards Lab](https://img.shields.io/badge/Bioinformatics-EdwardsLab-03A9F4)](https://edwards.flinders.edu.au/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub language count](https://img.shields.io/github/languages/count/linsalrob/pyctv)
[![PyPi](https://img.shields.io/pypi/pyversions/pyctv_taxonomy.svg?style=flat-square&label=PyPi%20Versions)](https://pypi.org/project/pyctv_taxonomy/)
[![DOI](https://www.zenodo.org/badge/611956728.svg)](https://www.zenodo.org/badge/latestdoi/611956728)
[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/pyctv_taxonomy/README.html)

# PyCTV Taxonomy

_We don't create the taxonomy, we just use it!_

The [ICTV](https://ictv.global/) [Virus Metadata Resource](https://ictv.global/vmr) contains an upto date taxonomy of viruses in Excel sheets. We parse that information, and make it available through a Python API

# VMR

The [ICTV](https://ictv.global/) maintains the Virus Metadata Resource, VMR, which is a list of all the viral taxonomies, connections to GenBank and RefSeq, and the associated metadata. This is, as far as I can tell, the most up-to-date list of all viral taxonomies.

PyCTV is designed to allow you to easily use the ICTVs VMR data in your own viral taxonomies!

When you first run it, you can `download` the viral taxonomy. But don't worry if you don't download it, because the first time you ask for it, we'll download it for you. The next time you run it, we'll let you know if there is a newer version that you should download. We parse that file, and create VMR objects which contain all the viral metadata resource information. You can query in a few different ways, and we provide `dicts` that map between GenBank IDs, RefSeq IDs, and the viral taxonomy. 

Viral taxonomy is generated using the now familiar notion of k\_\_, p\_\_, c\_\_ etc. abbreviations, and you can access the taxonomy as either a single string or tab separated text.

The most up-to-date version of the VMR can be found at [https://ictv.global/vmr/current/](https://ictv.global/vmr/current)

# Example uses

1. Download a new VMR dataset.

This places the VMR file in the [VMR](VMR/) folder in the distribution directory.

`pyctv.py download`

or you can force a new download (if you have an existing file you wish to replace):

`pyctv.py download --force`

[Note for Windows users: if you have the Excel file open you may get an error trying to delete it]

2. List all the viral species

List all the viruses separated by semi-colons:

`pyctv.py list --semi`

3. List all the GenBank accession numbers and the viral species

`pyctv.py list --genbank`

4. List all the RefSeq accession numbers and the viral species

`pyctv.py list --refseq`

# Install

We recommended the [conda installation](https://bioconda.github.io/recipes/pyctv_taxonomy/README.html):

```bash
conda install pyctv_taxonomy
```

You can `pip install pyctv_taxonomy` to get the latest version.

# Citing PyCTV

If you use PyCTV please cite:

```
Edwards, Robert A. (2023) PyCTV: A library for accessing the ICTV Virus Metadata Resource. Zenodo. DOI: https://doi.org/10.5281/zenodo.7728567
```

	
