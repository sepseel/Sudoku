class Sudoku:
    
    def __init__(self, spelbord):
        """
        constructor functie voor een spel sudoku, 
        baseert het spelbord op een string van 81 karakters,
        '-' voor een lege plek of cijfers.
        """
        if len(spelbord) != 81:
            raise AssertionError('ongeldig spelbord')
        self.maak_bord(spelbord)
        
    def __str__(self):
        """
        geeft de stringweergave van het spelbord trug, 
        met mooie dividers
        """
        string = ''
        for rij in range(9):
            if rij == 3 or rij == 6:
                string += '━━━━━━╋━━━━━━━╋━━━━━━\n'
            for kol in range(9):
                if kol == 3 or kol == 6:
                    string += '┃ '
                string += self.bord[rij][kol] + ' '
            string += '\n'
        return string
    
    def maak_bord(self, spelbord):
        """
        maakt een 2d array aan voor het spelbord op basis 
        van de gegeven string
        """
        self.bord = []
        rij = []
        for tegel in spelbord:
            rij.append(tegel)
            if len(rij) == 9:
                self.bord.append(rij)
                rij = []
        
    def vul_in(self, coord, waarde):
        """
        vult een waarde in op een lege plaats 
        als het een mogelijke zet is
        """
        rij = int(coord[0])
        kol = int(coord[2])
        waarde = str(waarde)
        if self.bord[rij][kol] != '-':
            raise AssertionError('tegel is al ingevuld')
        elif not self.check((rij, kol), waarde):
            raise AssertionError(waarde + ' kan niet worden ingevuld op ' + str(coord))
        self.bord[rij][kol] = waarde
        return self
        
    def check(self, coord, waarde):
        """
        kijkt na of een waarde op een gegeven plaats kan inngevuld worden,
        kijkt de rij, kolom en het vierkant na.
        geeft true als mogelijk
        """
        nietmogelijk = []
        nietmogelijk += self.check_rij(coord)
        nietmogelijk += self.check_kol(coord)
        nietmogelijk += self.check_vlak(coord)
        return str(waarde) not in nietmogelijk
        
    def check_rij(self, coord):
        """
        kijkt na welke waarden allemaal niet mogelijk zijn
        in de rij van gegeven coord
        """
        nm = []
        for i in self.bord[coord[0]]:
            nm.append(i)
        return nm
    
    def check_kol(self, coord):
        """
        kijkt na welke waarden allemaal niet mogelijk zijn
        in de kolom van gegeven coord
        """
        nm = []
        for i in range(9):
            nm.append(self.bord[i][coord[1]])
        return nm
    
    def check_vlak(self, coord):
        """
        kijkt na welke waarden allemaal niet mogelijk zijn 
        in het vlak van gegeven coord
        """
        nm = []
        coord = grenzen(coord)
        for rij in range(3):
            for kol in range(3):
                nm.append(self.bord[coord[0] + rij][coord[1] + kol])
        return nm
    
    def gewonnen(self):
        """
        kijkt na of er nog lege tegels zijn, anders is 
        het spel gewonnen
        """
        for rij in range(9):
            for kol in range(9):
                if self.bord[rij][kol] == '-':
                    return False
        return True
    
    def staat(self):
        """
        geeft een dict trug met de staat van het spel in beschreven, 
        voor een webimplementatie
        """
        spelbord = ''
        for rij in self.bord:
            for tegel in rij:
                spelbord += tegel
        staat = {
            "bord": self.bord,
            "spelbord": spelbord,
            "message": "proficiat, u heeft de sudoku opgelost!" * self.gewonnen()
        }
        return staat
    
def grenzen(coord):
    """
    geeft de ondergrenzen van coord trug, om hun bevattende
    vlak te kunen overlopen
    """
    rij = coord[0] - coord[0] % 3
    kol = coord[1] - coord[1] % 3
    return rij, kol