# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..convert import FSL2Scheme


def test_FSL2Scheme_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bscale=dict(argstr='-bscale %d',
    units='NA',
    ),
    bval_file=dict(argstr='-bvalfile %s',
    mandatory=True,
    position=2,
    ),
    bvec_file=dict(argstr='-bvecfile %s',
    mandatory=True,
    position=1,
    ),
    diffusiontime=dict(argstr='-diffusiontime %f',
    units='NA',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    flipx=dict(argstr='-flipx',
    ),
    flipy=dict(argstr='-flipy',
    ),
    flipz=dict(argstr='-flipz',
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    interleave=dict(argstr='-interleave',
    ),
    numscans=dict(argstr='-numscans %d',
    units='NA',
    ),
    out_file=dict(argstr='> %s',
    genfile=True,
    position=-1,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    usegradmod=dict(argstr='-usegradmod',
    ),
    )
    inputs = FSL2Scheme.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_FSL2Scheme_outputs():
    output_map = dict(scheme=dict(),
    )
    outputs = FSL2Scheme.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
