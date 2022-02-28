# Copyright alotofaxolotl (2022)
# under the GNU GPL ^3 license

import curses
from curses import wrapper


def matrix(stdscr):
	stdscr.clear()
	stdscr.addstr(0, 0, 'pymatrix')

	stdscr.refresh()
	key = stdscr.getkey()


def main():
	wrapper(matrix)

if __name__ == '__main__':
	main()

