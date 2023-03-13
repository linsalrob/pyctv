"""
Some simple helper functions we need
"""

import os
from pathlib import Path
from collections import OrderedDict

lib_directory = os.path.dirname(os.path.abspath(__file__))
# package_directory = Path(lib_directory).parent.absolute()
# for release, we will write the VMR file to the same directory as the library files
package_directory = lib_directory

def excel_columns():
    cols = OrderedDict()
    cols['Sort'] = 'species_sort'
    cols['Isolate Sort'] = 'isolate_sort'
    cols['Realm'] = 'realm'
    cols['Subrealm'] = 'subrealm'
    cols['Kingdom'] = 'kingdom'
    cols['Subkingdom'] = 'subkingdom'
    cols['Phylum'] = 'phylum'
    cols['Subphylum'] = 'subphylum'
    cols['Class'] = 'tax_class'
    cols['Subclass'] = 'subclass'
    cols['Order'] = 'order'
    cols['Suborder'] = 'suborder'
    cols['Family'] = 'family'
    cols['Subfamily'] = 'subfamily'
    cols['Genus'] = 'genus'
    cols['Subgenus'] = 'subgenus'
    cols['Species'] = 'species'
    cols['Exemplar or additional isolate'] = 'exemplar_or_additional_isolate'
    cols['Virus name(s)'] = 'virus_name'
    cols['Virus name abbreviation(s)'] = 'virus_name_abbreviation'
    cols['Virus isolate designation'] = 'virus_isolate_designation'
    cols['Virus GENBANK accession'] = 'virus_genbank_accession'
    cols['Virus REFSEQ accession'] = 'virus_refseq_accession'
    cols['Genome coverage'] = 'genome_coverage'
    cols['Genome composition'] = 'genome_composition'
    cols['Host source'] = 'host_source'

    return cols
