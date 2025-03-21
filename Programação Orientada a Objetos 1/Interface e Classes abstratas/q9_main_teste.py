from q2_tributavel_abs import Tributavel
from q6_correnteHeranca import ContaCorrente
from q7_seguroDeVida import SeguroDeVida

if	__name__	==	'__main__':
    cc	=	ContaCorrente('123-4',	'João',	1000.0)
    seguro	=	SeguroDeVida(100.0,	'José',	'345-77')
    print(cc.get_valor_imposto())
    print(seguro.get_valor_imposto())
