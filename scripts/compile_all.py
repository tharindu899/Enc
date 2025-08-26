import os, py_compile
errs = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.py'):
            path = os.path.join(root, f)
            try:
                py_compile.compile(path, doraise=True)
            except Exception as e:
                errs.append((path, repr(e)))
if not errs:
    print('ALL_OK')
else:
    for p, e in errs:
        print(p, e)
    raise SystemExit(1)
