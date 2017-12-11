# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import SurfaceSnapshots


def test_SurfaceSnapshots_inputs():
    input_map = dict(annot_file=dict(argstr='-annotation %s',
    xor=['annot_name'],
    ),
    annot_name=dict(argstr='-annotation %s',
    xor=['annot_file'],
    ),
    args=dict(argstr='%s',
    ),
    colortable=dict(argstr='-colortable %s',
    ),
    demean_overlay=dict(argstr='-zm',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    hemi=dict(argstr='%s',
    mandatory=True,
    position=2,
    ),
    identity_reg=dict(argstr='-overlay-reg-identity',
    xor=['overlay_reg', 'identity_reg', 'mni152_reg'],
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    invert_overlay=dict(argstr='-invphaseflag 1',
    ),
    label_file=dict(argstr='-label %s',
    xor=['label_name'],
    ),
    label_name=dict(argstr='-label %s',
    xor=['label_file'],
    ),
    label_outline=dict(argstr='-label-outline',
    ),
    label_under=dict(argstr='-labels-under',
    ),
    mni152_reg=dict(argstr='-mni152reg',
    xor=['overlay_reg', 'identity_reg', 'mni152_reg'],
    ),
    orig_suffix=dict(argstr='-orig %s',
    ),
    overlay=dict(argstr='-overlay %s',
    requires=['overlay_range'],
    ),
    overlay_range=dict(argstr='%s',
    ),
    overlay_range_offset=dict(argstr='-foffset %.3f',
    ),
    overlay_reg=dict(argstr='-overlay-reg %s',
    xor=['overlay_reg', 'identity_reg', 'mni152_reg'],
    ),
    patch_file=dict(argstr='-patch %s',
    ),
    reverse_overlay=dict(argstr='-revphaseflag 1',
    ),
    screenshot_stem=dict(),
    show_color_scale=dict(argstr='-colscalebarflag 1',
    ),
    show_color_text=dict(argstr='-colscaletext 1',
    ),
    show_curv=dict(argstr='-curv',
    xor=['show_gray_curv'],
    ),
    show_gray_curv=dict(argstr='-gray',
    xor=['show_curv'],
    ),
    six_images=dict(),
    sphere_suffix=dict(argstr='-sphere %s',
    ),
    stem_template_args=dict(requires=['screenshot_stem'],
    ),
    subject_id=dict(argstr='%s',
    mandatory=True,
    position=1,
    ),
    subjects_dir=dict(),
    surface=dict(argstr='%s',
    mandatory=True,
    position=3,
    ),
    tcl_script=dict(argstr='%s',
    genfile=True,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    truncate_overlay=dict(argstr='-truncphaseflag 1',
    ),
    )
    inputs = SurfaceSnapshots.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_SurfaceSnapshots_outputs():
    output_map = dict(snapshots=dict(),
    )
    outputs = SurfaceSnapshots.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
