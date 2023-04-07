import matplotlib.pyplot as plt
import os
import subprocess
import tempfile


class Animation:
    def __init__(self, tmp_path=None):
        self.tmp_path = tmp_path
        self._tmp_dir = None

        if self.tmp_path is None:
            self._tmp_dir = tempfile.TemporaryDirectory()
            self.tmp_path = self._tmp_dir.name

        self._frame_counter = 0

    def __del__(self):
        if self._tmp_dir:
            self._tmp_dir.cleanup()

    def add_figure(self, figure=None):
        if figure is not None:
            figure_tmp = plt.gcf().number
            plt.figure(figure.number)

        plt.savefig(os.path.join(self.tmp_path, f"{self._frame_counter}.png"))

        if figure is not None:
            plt.figure(figure_tmp)

        self._frame_counter += 1

    def export(self, output, delay=10):
        cmd = f"convert -delay {delay} -loop 0 $(ls -1 {self.tmp_path}/*.png | sort -V) {output}"
        subprocess.run(cmd, shell=True)
