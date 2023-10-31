import glob
import os
from pathlib import Path


if __name__ == '__main__':
    input_root_folder = \
        str(Path(__file__).parent.parent.parent) + os.sep + 'content' + os.sep + 'posts'

    recursive_globs_pattern = \
        '/**/*'

    input_file_paths = \
        glob.glob(
            pathname=input_root_folder + recursive_globs_pattern + '.md',
            recursive=True)

    for input_file_path in input_file_paths:
        pass
