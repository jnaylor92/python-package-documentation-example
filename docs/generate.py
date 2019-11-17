"""
Script to help auto generate Documentation
"""
import os
import shutil
import subprocess
import sys


class GenerateAPIDocs:
    BUILD_DIR = os.path.abspath(os.path.dirname(__file__))
    AUTODOC_DIR = os.path.join(BUILD_DIR, 'source', 'autodoc')
    ROOT = os.path.normpath(os.path.join(BUILD_DIR, '..'))
    SRC_DIR = os.path.join(ROOT, 'my_docs')

    def __init__(self):
        """
        Constructor
        """
        try:
            import sphinx as _
        except ImportError:
            exit('Generating API docs requires Sphinx')

    def run(self):
        """

        :return:
        """
        self.create_autodoc()
        curr_dir = os.curdir
        os.chdir(self.BUILD_DIR)
        ret_code = subprocess.call('make html', shell=os.name == 'nt')
        os.chdir(curr_dir)
        print(os.path.abspath(os.path.join(self.BUILD_DIR, 'build', 'html', 'index.html')))
        sys.exit(ret_code)

    def create_autodoc(self):
        """

        """
        print("Generating Autodoc")
        self._clean_directory(self.AUTODOC_DIR)
        cmd = ['sphinx-apidoc',
               '--output-dir', self.AUTODOC_DIR,
               '--force',
               '--no-toc',
               '--module-first',
               '--maxdepth', '2',
               self.SRC_DIR]
        print(" ".join(cmd))
        subprocess.call(cmd)

    @staticmethod
    def _clean_directory(dir_path):
        """

        :param dir_path:
        :return:
        """
        if os.path.exists(dir_path):
            print("Cleaning: \"{0}\"".format(dir_path))
            shutil.rmtree(dir_path)


def main():
    """

    :return:
    """
    GenerateAPIDocs().run()


if __name__ == "__main__":
    main()
