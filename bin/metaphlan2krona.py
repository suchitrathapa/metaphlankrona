#!/usr/bin/env python

# ============================================================================== 
# Conversion script: from MetaPhlAn output to Krona text input file
# Author: Daniel Brami (daniel.brami@gmail.com)
# ==============================================================================

import sys
import optparse
import csv

def main():
    #Parse Command Line
    parser = optparse.OptionParser()
    parser.add_option( '-p', '--profile', dest='profile', default='', action='store', help='The input file is the MetaPhlAn standard result file' )
    parser.add_option( '-k', '--krona', dest='krona', default='krona.out', action='store', help='the Krona output file name' )
    ( options, spillover ) = parser.parse_args()

    if not options.profile or not options.krona:
        parser.print_help()
        sys.exit()

    metaPhLan = list()
    metaPhLan_FH = open(options.profile,'r')
    metaPhLan = csv.DictReader(
        filter(lambda row: row[0]!='#', metaPhLan_FH),
        delimiter="\t",
        fieldnames=['clade_name','NCBI_tax_id','relative_abundance','additional_species']
        )

    krona_tmp = options.krona 
    krona_FH = open(krona_tmp, 'w')

    for row in metaPhLan:
        if "s__" in row['clade_name']:
            lineage = row['clade_name'].replace("|", "\t")
            abundance = float(row['relative_abundance'])

            krona_FH.write(f"{abundance}\t{lineage}\n")

    krona_FH.close()
    metaPhLan_FH.close()

if __name__ == '__main__':
    main()