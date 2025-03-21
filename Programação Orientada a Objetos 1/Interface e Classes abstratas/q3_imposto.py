import	abc

class Tributavel(abc.ABC):
	@abc.abstractmethod
	def	get_valor_imposto(self,	valor):
		pass