from bridge import Hand

x = Hand()
assert str(x) == '.............'

y = Hand('test')
assert str(y) == 'test'

x = Hand('akq.jt9.876.5432')
assert str(x) == 'abcqrsGHIWXYZ'

y = Hand('+-*./09.876.1111')
assert str(y) == 'abcqrsGHIZZZZ'
assert y.hcp() == 10

z = Hand('aq3.kj4.a543.q43')
assert z.hcp() == 16
