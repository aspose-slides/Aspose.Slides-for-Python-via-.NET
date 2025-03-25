from .access_child_node_specific_position import access_child_node_specific_position
from .access_child_nodes import access_child_nodes
from .access_smart_art import access_smart_art
from .access_smart_art_particular_layout import access_smart_art_particular_layout
from .access_smart_art_shape import access_smart_art_shape
from .add_nodes import add_nodes
from .add_nodes_specific_position import add_nodes_specific_position
from .assistant_node import assistant_node
from .bullet_fill_format_example import bullet_fill_format_example
from .change_smart_art_layout import change_smart_art_layout
from .change_smart_art_shape_color_style import change_smart_art_shape_color_style
from .change_smart_art_shape_style import change_smart_art_shape_style
from .change_smart_art_state import change_smart_art_state
from .change_text_on_smart_art_node import change_text_on_smart_art_node
from .check_smart_art_hidden_property import check_smart_art_hidden_property
from .create_smart_art_shape import create_smart_art_shape
from .custom_child_nodes_in_smart_art import custom_child_nodes_in_smart_art
from .fill_format_smart_art_shape_node import fill_format_smart_art_shape_node
from .organize_chart_layout_type import organize_chart_layout_type
from .remove_node_example import remove_node_example
from .remove_node_specific_position import remove_node_specific_position


def run_smart_arts_examples(global_opts):
    print("===== SmartArt examples =====")
    access_child_node_specific_position()
    access_child_nodes(global_opts)
    access_smart_art(global_opts)
    access_smart_art_particular_layout(global_opts)
    access_smart_art_shape(global_opts)
    add_nodes(global_opts)
    add_nodes_specific_position(global_opts)
    assistant_node(global_opts)
    bullet_fill_format_example(global_opts)
    change_smart_art_layout(global_opts)
    change_smart_art_shape_color_style(global_opts)
    change_smart_art_shape_style(global_opts)
    change_smart_art_state(global_opts)
    change_text_on_smart_art_node(global_opts)
    check_smart_art_hidden_property(global_opts)
    create_smart_art_shape(global_opts)
    custom_child_nodes_in_smart_art(global_opts)
    fill_format_smart_art_shape_node(global_opts)
    organize_chart_layout_type(global_opts)
    remove_node_example(global_opts)
    remove_node_specific_position(global_opts)
