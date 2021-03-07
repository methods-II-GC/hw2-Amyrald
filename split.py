#!/usr/bin/env python
"""One-line description of the program goes here."""
from typing import Iterator, List
import argparse

def read_tags(path: str) -> Iterator[List[List[str]]]:
    with open(path, "r") as source:
        lines = []
        for line in source:
            line = line.rstrip()
            if line:  # Line is contentful.
                lines.append(line.split())
            else:  # Line is blank.
                yield lines.copy()
                lines.clear()
    # Just in case someone forgets to put a blank line at the end...
    if lines:
        yield lines

def write_tag(data_set: list, file_tag: str) -> Iterator[List[List[str]]]:
    with open(file_tag, 'w') as filehandle:
        for row in data_set:
            for word in row:
                print(word, file = filehandle)       

def main(args: argparse.Namespace) -> None:
    corpus = list(read_tags(args.input))
    train_set = corpus[0: int(len(corpus)*0.8)-1]
    dev_set = corpus[int(len(corpus)*0.8) : int(-len(corpus)*0.1)]
    test_set = corpus[int(-len(corpus)*0.1): ]
    write_tag(train_set, args.train)
    write_tag(dev_set, args.dev)
    write_tag(test_set, args.test)
     # TODO: do the work here.
    ...

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help = "input file to the data")
    parser.add_argument("train")
    parser.add_argument("dev")
    parser.add_argument("test")
    main(parser.parse_args())

    # TODO: declare arguments.
    # TODO: parse arguments and pass them to `main`.
    ...
