# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..io import MySQLSink


def test_MySQLSink_inputs():
    input_map = dict(config=dict(mandatory=True,
    xor=['host'],
    ),
    database_name=dict(mandatory=True,
    ),
    host=dict(mandatory=True,
    requires=['username', 'password'],
    usedefault=True,
    xor=['config'],
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    password=dict(),
    table_name=dict(mandatory=True,
    ),
    username=dict(),
    )
    inputs = MySQLSink.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value

