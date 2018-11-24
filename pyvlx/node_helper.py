"""Helper module for Node objects."""
from .const import NodeTypeWithSubtype
from .opening_device import Window, Blind, RollerShutter


def convert_frame_to_node(pyvlx, frame):
    """Convert FrameGet[All]Node[s]InformationNotification into Node object."""
    if frame.node_type == NodeTypeWithSubtype.WINDOW_OPENER:
        return Window(pyvlx=pyvlx, node_id=frame.node_id, name=frame.name, rain_sensor=False)
    if frame.node_type == NodeTypeWithSubtype.WINDOW_OPENER_WITH_RAIN_SENSOR:
        return Window(pyvlx=pyvlx, node_id=frame.node_id, name=frame.name, rain_sensor=True)
    if frame.node_type == NodeTypeWithSubtype.ROLLER_SHUTTER:
        return RollerShutter(pyvlx=pyvlx, node_id=frame.node_id, name=frame.name)
    if frame.node_type == NodeTypeWithSubtype.VERTICAL_INTERIOR_BLINDS or \
            frame.node_type == NodeTypeWithSubtype.EXTERIOR_VENETIAN_BLIND or \
            frame.node_type == NodeTypeWithSubtype.LOUVER_BLIND:
        return Blind(pyvlx=pyvlx, node_id=frame.node_id, name=frame.name)

    pyvlx.logger.warning("%s not implemented", frame.node_type)
    return None