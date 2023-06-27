from random import *

class Bmx:
	
	def __init__(self, id, nombre, cuadro, manillar, horquilla, avance, dire) -> None:
			self.id = self.__gen_id()
			self.nombre = nombre
			self.cuadro = cuadro
			self.manillar = manillar
			self.horquilla = horquilla
			self.avance = avance
			self.dire = dire

	def get_nombre(self):
		return self.nombre

	def get_cuadro(self):
		return self.cuadro

	def get_manillar(self):
		return self.manillar

	def get_horquilla(self):
		return self.horquilla

	def get_avance(self):
		return self.avance

	def get_dire(self):
		return self.dire

	def get_id(self):
		return self.id


	def set_nombre(self, nombre_nuevo):
		self.nombre = nombre_nuevo

	def set_cuadro(self, cuadro_nuevo):
		self.cuadro = cuadro_nuevo
		
	def set_manillar(self, manillar_nuevo):
		self.manillar = manillar_nuevo

	def set_horquilla(self, horquilla_nuevo):
		self.horquilla = horquilla_nuevo

	def set_avance(self, avance_nuevo):
		self.avance = avance_nuevo

	def set_dire(self, dire_nuevo):
		self.dire = dire_nuevo

	def set_id(self, id_nuevo):
		self.id = id_nuevo
	
	def __gen_id(self):
		id = ""
		chars = "ABCDEFGHIJKLMNOPQRSTYWXZ1234567890"
		for _ in range(6):
			x = str(randint(0, len(chars)-1))
			id += x
		return id