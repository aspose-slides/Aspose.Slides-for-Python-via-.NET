from .add_vba_macros import add_vba_macros
from .extracting_vba_macros import extracting_vba_macros
from .remove_vba_macros import remove_vba_macros


def run_vba_examples(global_opts):
    print("===== VBA examples =====")
    add_vba_macros(global_opts)
    extracting_vba_macros(global_opts)
    remove_vba_macros(global_opts)
