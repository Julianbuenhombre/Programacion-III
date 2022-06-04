class Persona():

	def _init_(self, nombre, edad, Lugar_residencia):


		self.nombre=nombre
		self.edad=edad
		self.Lugar_residencia=Lugar_residencia

	def descripcion(self):

		print("Nombre: ", self.nombre, "Edad: ", self.edad, " Residencia: ", self.lugar_residencia)

	class Empleado(Persona):

		def _init_(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
            super()._init_(nombre_empleado, edad_empleado, residencia_empleado)


			self.salario=salario
			self.antigüedad=antigüedad

	    def descripcion(self):
	    	super().descripcion()
	    	print(" Salario: " , self.salario, " Antigüedad: ", self.antigüedad)


	Manuel=Empleado("Manuel", 55, "Colombia")
	Manuel.descripcion()
	print(isinstance(Manuel, Empleado))
