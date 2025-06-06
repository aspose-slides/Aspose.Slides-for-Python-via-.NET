from .add_color_to_data_points import charts_add_color_to_data_points
from .add_custom_color import charts_add_custom_error
from .add_doughnut_callout import charts_add_doughnut_callout
from .add_error_bars import charts_add_error_bars
from .adding_custom_lines import charts_adding_custom_lines
from .animating_categories_elements import charts_animating_categories_elements
from .animating_series import charts_animating_series
from .animating_series_elements import charts_animating_series_elements
from .automatic_chart_series_color import charts_automatic_chart_series_color
from .box_chart import charts_box_chart
from .calculate_formulas import charts_calculate_formulas
from .change_chart_category_axis import charts_change_chart_category_axis
from .change_color_of_categories import charts_change_color_of_categories
from .chart_data_cell_formulas import charts_data_cell_formulas
from .chart_data_point_index import chart_data_point_index
from .chart_entities import charts_entities_formatting
from .chart_get_range import charts_get_range
from .chart_get_layout import charts_get_layout
from .chart_manage_properties import charts_manage_properties
from .chart_marker_options_on_data_point import charts_marker_options_on_data_point
from .chart_recover_workbook import charts_recover_workbook
from .chart_trend_lines import charts_trend_lines
from .clear_specific_chart_series_data_points_data import charts_clear_specific_chart_series_datapoints_data
from .create_external_workbook import charts_create_external_workbook
from .data_source_type_property_added import charts_data_source_type_property_added
from .default_markers_in_chart import charts_default_markers
from .display_chart_labels import charts_display_chart_labels
from .display_percentage_as_labels import charts_display_percentage_as_labels
from .doughnut_chart_hole import charts_doughnut_chart_hole
from .edit_chart_data_in_external_workbook import charts_edit_chart_data_in_external_workbook
from .existing_chart import charts_existing_chart
from .font_properties_for_chart import charts_font_properties_for_chart
from .font_properties_for_invidual_legend import charts_font_properties_for_invidual_legend
from .font_size_legend import charts_font_size_legend
from .funnel_chart import charts_funnel_chart
from .get_actual_position_of_chart_data_label import charts_get_actual_position_of_chart_data_label
from .get_chart_image import charts_get_chart_image
from .get_values_and_unit_scale_from_axis import charts_get_values_and_unit_scale_from_axis
from .get_width_height_from_chart_plot_area import charts_get_width_height_from_chart_plot_area
from .hide_information_from_chart import charts_hide_information_from_chart
from .histogram_chart import charts_histogram_chart
from .invert_if_negative_for_individual_series import charts_series_invert_if_negative
from .map_chart import charts_map_chart
from .multi_category_chart import charts_multi_category_chart
from .normal_charts import charts_normal_charts
from .number_format import charts_number_format
from .organization_chart import charts_organization_chart
from .pie_chart import charts_pie_chart
from .radar_chart_creating import charts_radar_chart
from .scattered_chart import charts_scattered_chart
from .second_plot_options_for_charts import charts_second_plot_options
from .set_automatic_series_fill_color import charts_set_automatic_series_fill_color
from .set_category_axis_label_distance import charts_set_category_axis_label_distance
from .set_chart_series_overlap import charts_set_chart_series_overlap
from .set_data_labels_percentage_sign import charts_set_data_labels_percentage_sign
from .set_data_range import charts_set_data_range
from .set_external_workbook import charts_set_external_workbook
from .set_external_workbook_with_update_chart_data import charts_set_external_workbook_with_update_chart_data
from .set_gap_width import charts_set_gap_width
from .set_invert_fill_color_chart import charts_set_invert_fill_color_chart
from .set_layout_mode import charts_set_layout_mode
from .set_legend_custom_options import charts_set_legend_custom_options
from .set_marker_options import charts_set_marker_options
from .setting_automic_pie_chart_slice_colors import charts_setting_automic_pie_chart_slice_colors
from .setting_callout_for_data_label import charts_setting_callout_for_data_label
from .setting_data_format_for_category_axis import charts_setting_date_format_for_category_axis
from .setting_font_properties import charts_setting_font_properties
from .setting_position_axis import charts_setting_position_axis
from .setting_rotation_angle import charts_setting_rotation_angle
from .showing_display_unit_label import charts_showing_display_unit_label
from .sunburst_chart import charts_sunburst_chart
from .support_for_bubble_chart_scaling import charts_support_for_bubble_chart_scaling
from .support_for_changing_series_color import charts_changing_series_color
from .support_for_precision_of_data import charts_precision_of_data
from .support_for_stock_chart import charts_stock_chart
from .support_of_bubble_size_representation import charts_bubble_size_representation
from .time_unit_type_enum import charts_time_unit_type_enum
from .tree_map_chart import charts_tree_map_chart
from .using_workbook_chart_cell_as_data_label import charts_workbook_as_datalabel
from .validate_chart_layout_added import charts_validate_chart_layout
from .worksheet_example import charts_worksheets_example


def run_charts_examples(global_opts):
    print("===== Charts examples =====")
    charts_add_color_to_data_points(global_opts)
    charts_add_custom_error(global_opts)
    charts_add_doughnut_callout(global_opts)
    charts_add_error_bars(global_opts)
    charts_adding_custom_lines(global_opts)
    charts_animating_categories_elements(global_opts)
    charts_animating_series(global_opts)
    charts_animating_series_elements(global_opts)
    charts_automatic_chart_series_color(global_opts)
    charts_box_chart(global_opts)
    charts_calculate_formulas(global_opts)
    charts_change_chart_category_axis(global_opts)
    charts_change_color_of_categories(global_opts)
    charts_data_cell_formulas(global_opts)
    charts_entities_formatting(global_opts)
    charts_get_range()
    charts_get_layout()
    charts_manage_properties(global_opts)
    charts_marker_options_on_data_point(global_opts)
    charts_recover_workbook(global_opts)
    charts_trend_lines(global_opts)
    charts_clear_specific_chart_series_datapoints_data(global_opts)
    charts_create_external_workbook(global_opts)
    charts_data_source_type_property_added(global_opts)
    charts_default_markers(global_opts)
    charts_display_chart_labels(global_opts)
    charts_display_percentage_as_labels(global_opts)
    charts_doughnut_chart_hole(global_opts)
    # charts_edit_chart_data_in_external_workbook(options)
    charts_existing_chart(global_opts)
    charts_font_properties_for_chart(global_opts)
    charts_font_properties_for_invidual_legend(global_opts)
    charts_font_size_legend(global_opts)
    charts_funnel_chart(global_opts)
    charts_get_actual_position_of_chart_data_label(global_opts)
    charts_get_chart_image(global_opts)
    charts_get_values_and_unit_scale_from_axis(global_opts)
    charts_get_width_height_from_chart_plot_area(global_opts)
    charts_hide_information_from_chart(global_opts)
    charts_histogram_chart(global_opts)
    charts_series_invert_if_negative(global_opts)
    charts_map_chart(global_opts)
    charts_multi_category_chart(global_opts)
    charts_normal_charts(global_opts)
    charts_number_format(global_opts)
    charts_organization_chart(global_opts)
    charts_pie_chart(global_opts)
    charts_radar_chart(global_opts)
    charts_scattered_chart(global_opts)
    charts_second_plot_options(global_opts)
    charts_set_automatic_series_fill_color(global_opts)
    charts_set_category_axis_label_distance(global_opts)
    charts_set_chart_series_overlap(global_opts)
    charts_set_data_labels_percentage_sign(global_opts)
    # charts_set_data_range(global_opts)
    charts_set_external_workbook(global_opts)
    charts_set_external_workbook_with_update_chart_data(global_opts)
    charts_set_gap_width(global_opts)
    charts_set_invert_fill_color_chart(global_opts)
    charts_set_layout_mode(global_opts)
    charts_set_legend_custom_options(global_opts)
    charts_set_marker_options(global_opts)
    charts_setting_automic_pie_chart_slice_colors(global_opts)
    charts_setting_callout_for_data_label(global_opts)
    charts_setting_date_format_for_category_axis(global_opts)
    charts_setting_font_properties(global_opts)
    charts_setting_position_axis(global_opts)
    charts_setting_rotation_angle(global_opts)
    charts_showing_display_unit_label(global_opts)
    charts_sunburst_chart(global_opts)
    charts_support_for_bubble_chart_scaling(global_opts)
    charts_changing_series_color(global_opts)
    charts_precision_of_data(global_opts)
    charts_stock_chart(global_opts)
    charts_bubble_size_representation(global_opts)
    charts_time_unit_type_enum(global_opts)
    charts_tree_map_chart(global_opts)
    charts_workbook_as_datalabel(global_opts)
    charts_validate_chart_layout(global_opts)
    charts_worksheets_example(global_opts)
