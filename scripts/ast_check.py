import ast, sys
p = r"c:\Users\tharindu\Documents\Enc\bot\workers\downloaders\download.py"
s = open(p, 'r', encoding='utf-8').read()
try:
    ast.parse(s)
    print('PARSE_OK')
except SyntaxError as e:
    print(repr(e))
    print('lineno:', e.lineno)
    print('offset:', e.offset)
    print('text:', e.text)
    sys.exit(1)
