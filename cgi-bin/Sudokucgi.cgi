#!/home/sepseel/anaconda3/bin/python
##!/usr/bin/env python

from Sudoku import Sudoku
import cgitb
import cgi
import json

# geef meer informatie weer bij een request,
# zoals error boodschappen
cgitb.enable()

standaardbord = (
    '--8-----3' +
    '7------5-' +
    '-63-18-42' +
    '-5--2----' + 
    '4---9152-' +
    '---3-6--8' + 
    '---1---6-' + 
    '-9--4--8-' +
    '---68931-'
)

def new_game(spelbord=standaardbord):
    """
    start een niew spel met de opgegeven grootte
    """
    game = Sudoku(spelbord)
    print(json.dumps(game.staat()))

def do_move(status, waarde, coord):
    """
    maakt een zet op de opgegeven status met de gegeven kleur,
    en geeft de nieuwe status trug
    """
    status = json.loads(status)
    game = Sudoku(status["spelbord"])
    game.vul_in(coord, waarde)
    print(json.dumps(game.staat()))

def parse_query():
    """
    vertaald de query naar een uitvoerbare functie, 
    en voert deze uit
    """
    parameters = cgi.FieldStorage()
    func = parameters.getvalue('func')
    if func == 'new_game':
        return new_game()
    elif func == 'do_move':
        staat = parameters.getvalue('state')
        coord = parameters.getvalue('coord')
        waarde = parameters.getvalue('waarde')
        return do_move(staat, waarde, coord)

def print_bord(status):
    """
    print het spelbord uit naar de console 
    (voor debugging)
    """
    print(Sudoku(staat["spelbord"]))

print("Content-type: text/json\nAccess-Control-Allow-Origin: *\n")
parse_query()
