class Trabajador:
    def __init__(self, n_tbj, ctg, he, td):
        self.tbj = n_tbj
        self.ctg = ctg # ctg categoría
        self.he = he # he = horas extras
        self.td = td # td = tardanza
    def calcularSueldo(self):
        print(self.tbj)