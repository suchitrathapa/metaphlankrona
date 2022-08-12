process METAPHLAN2KRONA {
    tag "$meta.id"
    label 'process_small'

    conda (params.enable_conda ? 'bioconda::metaphlan=3.0.12' : null)
    container "${ workflow.containerEngine == 'singularity' && !task.ext.singularity_pull_docker_container ?
        'https://depot.galaxyproject.org/singularity/metaphlan:3.0.12--pyhb7b1952_0' :
        'quay.io/biocontainers/metaphlan:3.0.12--pyhb7b1952_0' }"

    input:
    tuple val(meta), path(taxa)

    output:
    tuple val(meta), path("*.output"), emit: krona_text

    script:
    """
    metaphlan2krona.py -p $taxa -k ${meta.id}.output
    """
}
