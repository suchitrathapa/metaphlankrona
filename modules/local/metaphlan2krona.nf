process METAPHLAN2KRONA {
    tag "$meta.id"
    label 'process_small'

    conda (params.enable_conda ? "conda-forge::python=3.8.3" : null)
    container "${ workflow.containerEngine == 'singularity' && !task.ext.singularity_pull_docker_container ?
        'https://depot.galaxyproject.org/singularity/python:3.8.3' :
        'quay.io/biocontainers/python:3.8.3' }"

    input:
    tuple val(meta), path(taxa)

    output:
    tuple val(meta), path("*.output"), emit: krona_text

    script:
    """
    metaphlan2krona.py -p $taxa -k ${meta.id}.output
    """
}
