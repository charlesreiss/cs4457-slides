#!/usr/bin/python3

from argparse import ArgumentParser
from pathlib import Path

import re

def write_qmds(base: Path, directory: Path, with_backup: bool = False):
    base_path = str(directory.relative_to(base))
    directory.mkdir()
    (directory / '_talk-inner.qmd').write_text('')
    if with_backup:
        (directory / '_talk-backup.qmd').write_text('')
    talk = f'---\nname: {directory.name}\n---\n'
    talk += '\n{{< include /' + base_path + '/_talk-inner.qmd >}}'
    if with_backup:
        talk += '\n# backup slides\n'
        talk += '\n{{< include /' + base_path + '/_talk-backup.qmd >}}'
    (directory / 'talk.qmd').write_text(talk)

def write_texfig(base: Path, path: Path):
    inner_path = path.with_name(path.name + '.inner.tex')
    figure_path = path.with_name(path.name + '.figure.tex')
    figure_template = r"""
\documentclass[tikz]{standalone}
\input{common/tikzBase}
\begin{document}
\setSlide{1}
\input{INNER_FILE}
\end{document}
"""
    figure_template = figure_template.replace("INNER_FILE", str(inner_path.relative_to(base)))
    inner_template = r"""
\begin{tikzpicture}
\end{tikzpicture}
"""
    figure_path.write_text(figure_template)
    inner_path.write_text(inner_template)


def main():
    parser = ArgumentParser()
    parser.add_argument('target', type=Path)
    parser.add_argument('--base', type=Path, default=Path('.'))
    parser.add_argument('--with-backup', action='store_true', dest='backup')
    parser.add_argument('--without-backup', action='store_false', dest='backup')
    parser.set_defaults(backup=None)
    args = parser.parse_args()
    if args.backup == None:
        args.backup = (re.match(r'^\d+$', args.target.name) is None)
    if '/texfig' in str(args.target.relative_to(args.base)):
        write_texfig(base=args.base, path=args.target)
    else:
        write_qmds(base=args.base, directory=args.target, with_backup=args.backup)

if __name__ == '__main__':
    main()
