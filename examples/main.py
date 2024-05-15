#!/usr/bin/env python3

import os
from src import *


class Options:
    def __init__(self, data_dir, out_dir):
        self.data_dir = data_dir
        self.out_dir = out_dir


def main():
    current_dir = os.path.dirname(__file__)
    # Last empty path component to ensure that trailing slash is added
    global_opts = Options(os.path.join(current_dir, "data", ""), os.path.join(current_dir, "out", ""))
    os.makedirs(global_opts.out_dir, exist_ok=True)

    run_activex_examples(global_opts)
    run_metered_examples(global_opts)
    run_charts_examples(global_opts)
    run_presentation_examples(global_opts)
    run_rendering_printing_examples(global_opts)
    run_shapes_examples(global_opts)
    run_slides_examples(global_opts)
    run_smart_arts_examples(global_opts)
    run_tables_examples(global_opts)
    run_text_examples(global_opts)
    run_vba_examples(global_opts)


if __name__ == "__main__":
    main()
