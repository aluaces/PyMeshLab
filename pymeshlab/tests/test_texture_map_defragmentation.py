import pymeshlab as ml
from . import samples_common

import pytest
from sys import platform


def test_texture_map_defragmentation():
    if platform == 'linux' or platform == 'win32':
        pytest.skip("test_texture_map_defragmentation filter does not work through pytest on linux and windows; skipping")
    print('\n')
    base_path = samples_common.samples_absolute_path()
    output_path = samples_common.test_output_path()
    ms = ml.MeshSet()

    ms.load_new_mesh(base_path + "bunny10k_textured.obj")
    #ms.save_current_mesh(output_path + "bunny_text_defrag.obj")

    ms.texture_map_defragmentation()

    ms.save_current_mesh(output_path + "bunny_text_defrag.obj")
