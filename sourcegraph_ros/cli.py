import argparse

from . import SearchContext
from . import _DEFAULT_INDEX_URL
from .rosdistro import Index


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--distro", required=True)
    parser.add_argument("--index-url", default=_DEFAULT_INDEX_URL)
    return parser.parse_args()


def main():
    args = parse_args()

    index = Index.from_url(args.index_url)
    distro = index.get_distro(args.distro)
    if distro is None:
        print(index.distro_names)
        raise RuntimeError(f"Could not find distro {distro}")

    print(SearchContext.from_rosdistro(distro).json())


if __name__ == "__main__":
    main()