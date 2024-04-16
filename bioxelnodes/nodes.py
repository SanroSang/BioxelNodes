
from pathlib import Path
from .custom_nodes import CustomNodes
import bpy


def add_driver_to_node_factory(source_prop, target_prop):
    callback_str = f"""
import bpy
from bioxelnodes.utils import add_direct_driver, get_bioxels_obj
bioxels_obj = get_bioxels_obj(bpy.context.active_object)
if bioxels_obj:
    add_direct_driver(
        target=node,
        target_prop='{target_prop}',
        source=bioxels_obj,
        source_prop='{source_prop}'
    )
else:
    print('Cannot find any bioxels.')
    """
    return callback_str


MENU_ITEMS = [
    {
        'label': 'Present',
        'icon': 'MESH_MONKEY',
        'items': [
            {
                'label': 'Segment',
                'icon': 'OUTLINER_OB_META',
                'node_type': 'BioxelNodes_Segment',
                'node_description': '',
                'node_callback': add_driver_to_node_factory("value_offset", "Offset")
            }
        ]
    },
    {
        'label': 'Segment',
        'icon': 'OUTLINER_DATA_VOLUME',
        'items': [
            {
                'label': 'Segment by Level',
                'icon': 'AREA_JOIN',
                'node_type': 'BioxelNodes_SegmentByLevel',
                'node_description': '',
                'node_callback': add_driver_to_node_factory("value_offset", "Offset")
            },
            {
                'label': 'Segment by Range',
                'icon': 'AREA_SWAP',
                'node_type': 'BioxelNodes_SegmentByRange',
                'node_description': '',
                'node_callback': add_driver_to_node_factory("value_offset", "Offset")
            },
            {
                'label': 'Segment by Layers',
                'icon': 'OUTLINER_OB_FORCE_FIELD',
                'node_type': 'BioxelNodes_SegmentsByLayers',
                'node_description': '',
                'node_callback': add_driver_to_node_factory("value_offset", "Offset")
            }
        ]
    },
    {
        'label': 'Shader',
        'icon': 'SHADING_RENDERED',
        'items': [
            {
                'label': 'Segment Shader',
                'icon': 'OUTLINER_OB_VOLUME',
                'node_type': 'BioxelNodes_SegmentShader',
                'node_description': ''
            }
        ]
    },
    {
        'label': 'Slicer',
        'icon': 'CLIPUV_DEHLT',
        'items': [
            {
                'label': 'LPS Slicer',
                'icon': 'EMPTY_DATA',
                'node_type': 'BioxelNodes_LPS-Slicer',
                'node_description': '',
                'node_callback': add_driver_to_node_factory("image_origin", "Origin")
            },
            {
                'label': 'Axis Slicer',
                'icon': 'OUTLINER_OB_EMPTY',
                'node_type': 'BioxelNodes_AxisSlicer',
                'node_description': '',
            },
            {
                'label': 'Box Slicer',
                'icon': 'MOD_WIREFRAME',
                'node_type': 'BioxelNodes_BoxSlicer',
                'node_description': '',
            }
        ]
    },
]

custom_nodes = CustomNodes(
    menu_items=MENU_ITEMS,
    nodes_file=Path(__file__).parent/"assets/Nodes.blend",
    root_label='BioxelNodes',
    root_icon="FILE_VOLUME",
)
