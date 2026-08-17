import lark

import convert_lark

def _extract_overlays(tikz_code: str) -> list[str] | None:
    if 'overlay' not in tikz_code:
        return
    if 'remember picture' not in tikz_code:
        return
    m = re.match(r'''\s*
        \\begin\{tikzpicture\}(?:\[[^\]]+\])?
        \s*
            (?P<inside>(?s:.*?))
        \s*
        \\end\{tikzpicture\}
        \s*
    ''', tikz_code)
    assert m is not None, tikz_code
    tikz_code = m.group('inside')
    options: list[tuple[str, str]] = []
    result: list[str] = []
    while len(tikz_code):
        m = re.match(r'\\s+', tikz_code)
        if m is not None:
            tikz_code = tikz_code[m.end():]
            continue
        m = re.match(r'''
            \\tikzset\{
                (?P<options>
                    (?:
                        [^}]+
                    |
                        \{\[^}]*\}
                    )*
                )
            \}
        ''', tikz_code, re.X)
        if m is not None:
            options += re.findall(r'''
                (?P<name>[^=,]+)
                (?:
                    =(?P<value>
                        (?:
                            [^,]+|
                            \{[^}]\}
                        )
                    )
                )
            ''', m.group('options'))
            tikz_code = tikz_code[m.end():]
        m = re.match(r'''
            \\begin\{visibleenv\}<(?P<when>[^>]+)>
            \\node[(?P<options>[^]]+)\]\s*
                (?:\((?P<name>[^)]+\))?\s*
                at\s*
                (?:\((?:\[(?P<offset>[^\]])\])?(?P<loc>.*)\)\s*
                \{(?P<text>[^\}]+)\}\s*\;
            \\end\{visibleenv\}
            ''')
        if m is not None:
            text = m.group('text').replace('\\\\', ' ')
            text = re.sub(r'\\myemph\{(.*)\}', ' '
            result.append(
                '
