#!/usr/bin/env python3

"""Given a bunch of errors, and a json configuration, comment out the repos with errors."""

import argparse
import re


def comment_repos(json_text, repo_list):
    # [('/*', pos), ...]
    inserts = []
    for repo in repo_list:
        r_pos = json_text.find(repo)
        if r_pos == -1:
            raise ValueError(repo)
        ob_pos = json_text.rfind("{", 0, r_pos)
        cb_pos = json_text.find("},", r_pos)

        if ob_pos == -1:
            raise ValueError(repo)

        # Means could not find last entry in json
        # Switch offsets to make sure previous comma is commented out too
        if cb_pos == -1:
            # Find last }, or last */ if previous was commented out too
            ob_pos = json_text.rfind("},", 0, r_pos) + 1
            cb_pos = json_text.find("}", r_pos) + 1
        else:
            cb_pos += 2

        inserts.append(("/*", ob_pos))
        inserts.append(("*/", cb_pos))

    inserts = sorted(inserts, key=lambda t: t[1])

def remove_repos(json_text, repo_list):
    # [(start, end), ...]
    removals = []
    for repo in repo_list:
        r_pos = json_text.find(repo)
        if r_pos == -1:
            raise ValueError(repo)
        ob_pos = json_text.rfind("{", 0, r_pos)
        cb_pos = json_text.find("},", r_pos)

        if ob_pos == -1:
            raise ValueError(repo)

        if cb_pos == -1:
            cb_pos = json_text.find("}", r_pos) + 1
        else:
            cb_pos += 2

        removals.append((ob_pos, cb_pos))

    removals = sorted(removals, key=lambda t: t[0])

    new_text = []
    last_pos = 0
    for s, e in removals:
        new_text.append(json_text[last_pos:s])
        last_pos = e

    new_text.append(json_text[last_pos:])

    return "".join(new_text)


def repos_with_errors(errors_text):
    cannot_find_regex = re.compile("Cannot find (.+) repository")
    repos = []
    for repo in cannot_find_regex.findall(errors_text):
        repos.append(repo)
    return repos


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-file", required=True)
    parser.add_argument("--errors-file", required=True)
    return parser.parse_args()


def main():
    args = parse_args()

    with open(args.json_file) as jf:
        json_text = jf.read()

    with open(args.errors_file) as ef:
        errors_text = ef.read()

    print(remove_repos(json_text, repos_with_errors(errors_text)))


if __name__ == '__main__':
    main()