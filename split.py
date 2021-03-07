#!/usr/bin/env python
"""This programs takes in an input file containing text data then splits it and outputs a train set (80%), a develpoment set (10%) and a test set (10%)."""

from typing import Iterator, List
import argparse
import random

#Generator function takes in a file path and creates a text data in nested lists
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

#Writes text data in nested lists into a new file
def write_tag(data_set: list, file_tag: str) -> Iterator[List[List[str]]]:
    with open(file_tag, 'w') as filehandle:
        for row in data_set:
            for sent in row:
                print(sent, file = filehandle)   
      
#Command line argument parsers
def main(args: argparse.Namespace) -> None:
    corpus = list(read_tags(args.input))
    random.shuffle(corpus)
    train_set = corpus[0: int(len(corpus)*0.8)-1]
    dev_set = corpus[int(len(corpus)*0.8) : int(-len(corpus)*0.1)]
    test_set = corpus[int(-len(corpus)*0.1): ]
    write_tag(train_set, args.train)
    write_tag(dev_set, args.dev)
    write_tag(test_set, args.test)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help = "input file to the data")
    parser.add_argument("train", help = "Outputs train set")
    parser.add_argument("dev", help = "Outputs dev set")
    parser.add_argument("test", help = "Outputs test set")
    main(parser.parse_args())
