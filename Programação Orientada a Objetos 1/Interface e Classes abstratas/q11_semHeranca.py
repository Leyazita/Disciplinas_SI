class ContaCorrente(self):
	def	get_valor_imposto(self):
	    return	self._saldo	*	0.01
 
 
class SeguroDeVida(self):
    def	__init__(self,	valor,	titular,	numero_apolice):
        self._valor	= valor
        self._titular =	titular
        self._numero_apolice =	numero_apolice
    
    def	get_valor_impostoS(self):
        return	50	+	self._valor	*	0.05
    
    
if	__name__	==	'__main__':
    from	tributavel	import	Tributavel
    cc	=	ContaCorrente('João',	'123-4')
    cc.deposita(1000.0)
    seguro	=	SeguroDeVida(100.0,	'José',	'345-77')
    Tributavel.register(ContaCorrente)
    Tributavel.register(SeguroDeVida)
    lista_tributaveis	=	[]
    lista_tributaveis.append(cc)
    lista_tributaveis.append(seguro)
    mt	=	ManipuladorDeTributaveis()
    total	=	mt.calcula_impostos(lista_tributaveis)
    print(total)
