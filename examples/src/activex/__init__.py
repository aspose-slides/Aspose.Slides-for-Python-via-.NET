from .manage_activex_control import manage_activex_control
from .linking_video_activex_control import linking_video_activex_control


def run_activex_examples(global_opts):
    print("===== ActiveX examples =====")
    manage_activex_control(global_opts)
    linking_video_activex_control(global_opts)
