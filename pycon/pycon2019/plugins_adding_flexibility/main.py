import pathlib

import click
import matplotlib.pyplot as plt

import readers


def read_data(file_path, *args):
    """read data return a Pandas DataFrame"""
    file_format = file_path.suffix.lstrip(".")
    return readers.read(file_format, file_path, *args)


def create_plot(data):
    """plot Pandas DataFrame"""
    data.plot()
    plt.show()


@click.command()
@click.argument("file_path")
@click.option('--delimiter', help='delimiter for csv')
def main(file_path, delimiter):
    """read data and create a simple plot"""
    file_path = pathlib.Path(file_path)
    data = read_data(file_path, delimiter)
    create_plot(data)


if __name__ == '__main__':
    main()
