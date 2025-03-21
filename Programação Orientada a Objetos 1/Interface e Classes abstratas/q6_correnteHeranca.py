from q2_tributavel_abs import Tributavel

class ContaCorrente(Tributavel):
	def	get_valor_imposto(self):
	    return	self._saldo	*	0.01
