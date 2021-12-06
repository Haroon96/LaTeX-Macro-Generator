import json

def update_macro(name, value):
    # load macros from disk
    try:
        with open('macros.json') as f:
            js = json.load(f)
    except FileNotFoundError as e:
        js = {}

    # update macro value
    js[name] = value

    # write macros back to disk
    with open('macros.json', 'w') as f:
        json.dump(js, f)

    # write tex file
    with open('macros.tex', 'w') as t:
        t.write('%% AUTO GENERATED FILE\n')
        for k, v in js.items():
            v = str(v).replace('%', '\%')
            t.write('\\newcommand{\\%s}{%s}\n' % (k, v))
