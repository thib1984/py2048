"""
py2048 use case
"""

import columnar
import curses
import random

def app():
    def main(stdscr):

        curses.curs_set(0) 

        tableau = initialise_jeu()
        tour=0
        while True:
            ajoute_case(tableau)  
            tour=tour+1
            stdscr.clear()
            affiche_plateau(stdscr, tableau, tour)
            stdscr.refresh()
            end=False
            while True:
                key = stdscr.getch()
                if key == ord('q'):
                    end=True
                    break
                elif key == curses.KEY_UP:
                    break
                elif key == curses.KEY_DOWN:
                    break
                elif key == curses.KEY_LEFT:
                    break
                elif key == curses.KEY_RIGHT:
                    break
            if end:
                break
        
        
    curses.wrapper(main)

def ajoute_case(tableau):
    cases_vides = [(i, j) for i, ligne in enumerate(tableau) for j, element in enumerate(ligne) if element[0] == 0]
    if cases_vides:
        i, j = random.choice(cases_vides)
        nouvelle_valeur = random.choice([2, 4])
        tableau[i][j] = (nouvelle_valeur, tableau[i][j][1])


def affiche_plateau(stdscr, tableau, tour):
    
    data = [[element[0] for element in ligne] for ligne in tableau]
    table = columnar.columnar(data, no_borders=False)
    lines = table.split('\n')
    for i, line in enumerate(lines):
        stdscr.addstr(i, 0, line)
    
    
    stdscr.addstr(10, 0, str(tour))
    somme = sum(element[0] for ligne in tableau for element in ligne)
    stdscr.addstr(11, 0, str(somme))
    
def initialise_jeu():
    tableau = [[(0, False) for j in range(4)] for i in range(4)]
    return tableau