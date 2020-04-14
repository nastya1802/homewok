class Road:
    def mass_calculation (self, _lehgth, _weight, mass, thickness):
        self._lehgth = _lehgth
        self._weight = _weight
        self.mass = mass
        self.thickness = thickness
        return self._lehgth * self._weight * self.mass * self.thickness

calculation = Road ()
print(calculation.mass_calculation(20,5000,25,0.005))
