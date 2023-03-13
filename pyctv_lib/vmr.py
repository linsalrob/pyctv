

class VMR:
    """
    A record from the VMR file.

    We store all the information from the VMR file as these objects.

    There is a major caveat: `class` is a reserved word, so we use tax_class. Then for consistency we use
    tax_ for all the other names too.
    """
    def __init__(self, species_sort: str = None, isolate_sort: str = None, realm: str = None, subrealm: str = None,
                 kingdom: str = None, subkingdom: str = None, phylum: str = None, subphylum: str = None,
                 tax_class: str = None, subclass: str = None, order: str = None, suborder: str = None,
                 family: str = None, subfamily: str = None, genus: str = None, subgenus: str = None,
                 species: str = None, exemplar_or_additional_isolate: str = None, virus_name: str = None,
                 virus_name_abbreviation: str = None, virus_isolate_designation: str = None,
                 virus_genbank_accession: str = None, virus_refseq_accession: str = None, genome_coverage: str = None,
                 genome_composition: str = None, host_source: str = None):
        """
        Define a new VMR object
        """
        self.species_sort = species_sort
        self.isolate_sort = isolate_sort
        self.realm = realm
        self.subrealm = subrealm
        self.kingdom = kingdom
        self.subkingdom = subkingdom
        self.phylum = phylum
        self.subphylum = subphylum
        self.tax_class = tax_class
        self.subclass = subclass
        self.order = order
        self.suborder = suborder
        self.family = family
        self.subfamily = subfamily
        self.genus = genus
        self.subgenus = subgenus
        self.species = species
        self.tax_realm = realm
        self.tax_subrealm = subrealm
        self.tax_kingdom = kingdom
        self.tax_subkingdom = subkingdom
        self.tax_phylum = phylum
        self.tax_subphylum = subphylum
        self.tax_subclass = subclass
        self.tax_order = order
        self.tax_suborder = suborder
        self.tax_family = family
        self.tax_subfamily = subfamily
        self.tax_genus = genus
        self.tax_subgenus = subgenus
        self.tax_species = species
        self.exemplar_or_additional_isolate = exemplar_or_additional_isolate
        self.virus_name = virus_name
        self.virus_name_abbreviation = virus_name_abbreviation
        self.virus_isolate_designation = virus_isolate_designation
        self.virus_genbank_accession = virus_genbank_accession
        self.virus_refseq_accession = virus_refseq_accession
        self.genome_coverage = genome_coverage
        self.genome_composition = genome_composition
        self.host_source = host_source

    def __str__(self):
        s = f"r__{self.realm};k__{self.kingdom};p__{self.phylum};c__{self.tax_class};o__{self.order};"
        s += f"f__{self.family};g__{self.genus};s__{self.species}"
        return s

    def __eq__(self, other):
        return 0

    def __repr__(self):
        return str(self.__dict__)

    def __hash__(self):
        return hash(repr(self))

    def tsv(self):
        s = f"r__{self.realm}\tk__{self.kingdom}\tp__{self.phylum}\tc__{self.tax_class}\to__{self.order}\t"
        s += f"f__{self.family}\tg__{self.genus}\ts__{self.species}"
        return s

    def set_attributes(self, d):
        for k, v in d.items():
            setattr(self, k, v)