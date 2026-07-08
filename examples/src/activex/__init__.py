from .manage_activex_control_pillow_example import manage_activex_control_pillow_example
from .manage_activex_control_skia_example import manage_activex_control_skia_example
from .linking_video_activex_control import linking_video_activex_control


def run_activex_examples(global_opts):
    print("===== ActiveX examples =====")
    manage_activex_control_pillow_example(global_opts)
    manage_activex_control_skia_example(global_opts)
    linking_video_activex_control(global_opts)
