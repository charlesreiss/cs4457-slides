#!/usr/bin/python3
import argparse
from pathlib import Path

def fixup_texfig(old_texfig_base: str, old_texfig_dir: Path, new_texfig_base: str, new_texfig_dir: Path):
    inner_texfig = new_texfig_dir / (new_texfig_base + '.inner.tex')
    figure_texfig = new_texfig_dir / (new_texfig_base + '.figure.tex')

    base_dir = Path(__file__).parent
    old_texfig_relative = old_texfig_dir.relative_to(base_dir)
    new_texfig_relative = new_texfig_dir.relative_to(base_dir)

    figure_texfig_code = figure_texfig.read_text()
    figure_texfig_code = figure_texfig_code.replace(
        f'{old_texfig_relative}/{old_texfig_base}.inner',
        f'{new_texfig_relative}/{new_texfig_base}.inner'
    )
    figure_texfig.write_text(figure_texfig_code)

    inner_texfig_code = inner_texfig.read_text()
    inner_texfig_code = inner_texfig_code.replace(
        # \includegraphics{basedir/foo}, etc.
        '{' + str(old_texfig_relative),
        '{' + str(new_texfig_relative)
    )
    inner_texfig.write_text(inner_texfig_code)

def fixup_texfig_base(texfig_dir: Path, texfig_base) -> str:
    if not (texfig_dir / (texfig_base + '.inner.tex')).exists():
        candidates = list(texfig_dir.glob(f'{texfig_base}.inner.tex'))
        if len(candidates) > 1:
            raise Exception(f'too many candidates: {candidates}')
        if len(candidates) == 0:
            raise Exception(f'could not find {texfig_base} in {texfig_dir}')
        return candidates[0].name.replace('.inner.tex', '')
    else:
        return texfig_base

def move_texfig(old_texfig_base: str,  old_texfig_dir: Path, new_texfig_base: str, new_texfig_dir: Path):
    (old_texfig_dir / (old_texfig_base + '.inner.tex')).rename(new_texfig_dir / (new_texfig_base + '.inner.tex'))
    (old_texfig_dir / (old_texfig_base + '.figure.tex')).rename(new_texfig_dir / (new_texfig_base + '.figure.tex'))

def fixup_qmds_for_texfig(old_texfig_base: str, old_texfig_dir: Path, new_texfig_base: str, new_texfig_dir: Path):
    base_dir = Path(__file__).parent
    old_texfig_relative = old_texfig_dir.relative_to(base_dir)
    new_texfig_relative = new_texfig_dir.relative_to(base_dir)
    old_path = f'/{old_texfig_relative}/{old_texfig_base}'
    new_path = f'/{new_texfig_relative}/{new_texfig_base}'
    print(f'{old_path} -> {new_path}')
    for qmd in new_texfig_dir.parent.glob('*.qmd'):
        print(f'checking {qmd}')
        source = qmd.read_text()
        if old_path in source:
            source = source.replace(old_path, new_path)
            qmd.write_text(source)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--from-dir', type=Path)
    parser.add_argument('--to-dir', type=Path, default=None)
    parser.add_argument('--from-texfig', type=str)
    parser.add_argument('--to-texfig', type=str, default=None)
    parser.add_argument('--fixup-only', default=False, action='store_true')
    parser.add_argument('--exact', default=False, action='store_true')
    args = parser.parse_args()
    args.from_dir = args.from_dir.absolute()
    if args.to_dir is None:
        args.to_dir = args.from_dir
    args.to_dir = args.to_dir.absolute()
    if not args.exact:
        if not args.fixup_only:
            args.from_texfig = fixup_texfig_base(args.from_dir / 'texfig', args.from_texfig)
        else: # already moved
            if args.to_texfig is None:
                args.from_texfig = fixup_texfig_base(args.to_dir / 'texfig', args.from_texfig)
            else:
                args.to_texfig = fixup_texfig_base(args.to_dir / 'texfig', args.to_texfig)
    if args.to_texfig is None:
        args.to_texfig = args.from_texfig
    steps = []
    if not args.fixup_only:
        steps.append(move_texfig)
    steps += [fixup_texfig, fixup_qmds_for_texfig]
    for step in steps:
        step(
            old_texfig_base=args.from_texfig,
            old_texfig_dir=args.from_dir / 'texfig',
            new_texfig_base=args.to_texfig,
            new_texfig_dir=args.to_dir / 'texfig',
        )


if __name__ == '__main__':
    main()
