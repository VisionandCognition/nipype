# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..odf import MESD


def test_MESD_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bgmask=dict(argstr='-bgmask %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fastmesd=dict(argstr='-fastmesd',
    requires=['mepointset'],
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-inputfile %s',
    mandatory=True,
    position=1,
    ),
    inputdatatype=dict(argstr='-inputdatatype %s',
    ),
    inverter=dict(argstr='-filter %s',
    mandatory=True,
    position=2,
    ),
    inverter_param=dict(argstr='%f',
    mandatory=True,
    position=3,
    units='NA',
    ),
    mepointset=dict(argstr='-mepointset %d',
    units='NA',
    ),
    out_file=dict(argstr='> %s',
    genfile=True,
    position=-1,
    ),
    scheme_file=dict(argstr='-schemefile %s',
    mandatory=True,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = MESD.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MESD_outputs():
    output_map = dict(mesd_data=dict(),
    )
    outputs = MESD.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
