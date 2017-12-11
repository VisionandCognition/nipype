# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..featuredetection import TextureMeasureFilter


def test_TextureMeasureFilter_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    distance=dict(argstr='--distance %d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    inputMaskVolume=dict(argstr='--inputMaskVolume %s',
    ),
    inputVolume=dict(argstr='--inputVolume %s',
    ),
    insideROIValue=dict(argstr='--insideROIValue %f',
    ),
    outputFilename=dict(argstr='--outputFilename %s',
    hash_files=False,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = TextureMeasureFilter.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_TextureMeasureFilter_outputs():
    output_map = dict(outputFilename=dict(),
    )
    outputs = TextureMeasureFilter.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
