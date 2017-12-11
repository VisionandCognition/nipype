# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..minc import XfmAvg


def test_XfmAvg_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    avg_linear=dict(argstr='-avg_linear',
    ),
    avg_nonlinear=dict(argstr='-avg_nonlinear',
    ),
    clobber=dict(argstr='-clobber',
    usedefault=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    ignore_linear=dict(argstr='-ignore_linear',
    ),
    ignore_nonlinear=dict(argstr='-ignore_nonline',
    ),
    input_files=dict(argstr='%s',
    mandatory=True,
    position=-2,
    sep=' ',
    ),
    input_grid_files=dict(),
    output_file=dict(argstr='%s',
    genfile=True,
    position=-1,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    verbose=dict(argstr='-verbose',
    ),
    )
    inputs = XfmAvg.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_XfmAvg_outputs():
    output_map = dict(output_file=dict(),
    output_grid=dict(),
    )
    outputs = XfmAvg.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
