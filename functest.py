from bridge import Hand

x = Hand()
assert str(x) == '.............'

y = Hand('test')
assert str(y) == 'test'

z = Hand('test'*4)
try:
    assert str(z) == 'test'*4
except AssertionError:
    # expected failure
    print ('str(z) failed')

x = Hand('akq.jt9.876.5432')
assert str(x) == 'akq.jt9.876.5432'
