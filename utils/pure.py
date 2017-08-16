def showobj(value, label=None):
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    print('=' * 15, '{} type: {}'.format(label or '', type(value)), '=' * 15)
    pp.pprint(value)
    print()
