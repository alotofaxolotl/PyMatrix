#!/usr/bin/env python3

# Copyright alotofaxolotl (2022)
# under the GNU GPL ^3 license

import curses
from curses import wrapper
import random, time
import sys
import string
import os

charsets = {
	'japanese': 'あかさたなはまやらわいきしちにひみりうくすつぬふむゆるえけせてねへめれおこそとのほもよろん',
	'classic': string.printable[:84] # The ascii table excluding brackets and control chars
}


charset = charsets['japanese']
rows = 0
cols = 0
frequency = 1
density = 2
tail_range = (5, 20)
speed = 0.07


heads = []
tails = []

sets = {
	'cl': charsets['classic'],
	'jp': charsets['japanese']
}


def random_character():
	char = ' '
	while char == ' ':
		char = random.choice(charset)
	return char


def clear_screen(stdscr):
	for y in range(rows):
		stdscr.addstr(y, 0, ' ' * (cols-1))


def random_even_number(min, max):
	return random.randint(int(min/2), int(max/2)) * 2


class tail:

	def __init__(self, y, x, character, life):
		self.x = x
		self.y = y
		self.character = character
		self.life = life

	def update(self):
		self.life -= 1


class head:

	def __init__(self) -> None:
		self.y = -1
		self.x = random_even_number(0, cols - 1)
		self.length = random.randint(tail_range[0], tail_range[1])
		self.character = random_character()

	def move(self) -> None:

		self.y += 1
		self.character = random_character()


def add_head():
	h0 = None
	while True:
		found = True
		h0 = head()
		for h in heads:
			if h.x == h0.x and h.y - h.length < 2:
				found = False
				break
		if found:
			break
	heads.append(h0)


def matrix(stdscr):
	global rows, cols

	rows, cols = stdscr.getmaxyx()
	timer = 0

	curses.curs_set(0)

	while True:

		clear_screen(stdscr)

		if timer < frequency:
			timer += 1
		else:
			timer = 0
			for _ in range(density):
				add_head()

		# Tail Logic
		for t in tails:
			t.update()
			if t.life <= 0:
				tails.pop(tails.index(t))
			try:
				stdscr.addstr(t.y, t.x, t.character)
			except curses.error:
				pass

		# Head Logic
		for h in heads:
			if h.y > -1:
				tails.append(tail(h.y+1, h.x, h.character, h.length))
			h.move()
			if h.y >= rows - 1:
				heads.pop(heads.index(h))
			try:
				stdscr.addstr(h.y, h.x, h.character, curses.A_BOLD)
			except curses.error:
				pass

		stdscr.refresh()
		time.sleep(speed)


def read_args():

	global charset, frequency, density

	try:
		for i in range(len(sys.argv)):
			if sys.argv[i] == '-set':
				if sys.argv[i+1] in sets:
					charset = sets[sys.argv[i+1]]
			elif sys.argv[i] == '-f':
				frequency = int(sys.argv[i+1])
			elif sys.argv[i] == '-d':
				density = int(sys.argv[i+1])
	except Exception:
		print('Invalid arguments!')
		return


def read_rc():

	global charset, frequency, density

	path = os.path.expanduser('~') + '/.pymatrixrc'
	
	try:
		with open(path, 'r') as rc:
			for line in rc:
				l = line.rstrip('\n').replace(' ', '').split('=')
				if l[0] == 'SET':
					if l[1] in sets:
						charset = sets[l[1]]
				elif l[0] == 'DENSITY':
					density = int(l[1])
				elif l[0] == 'FREQUENCY':
					frequency = int(l[1])
	except Exception:
		return


def main():

	read_rc()
	read_args()

	try:
		wrapper(matrix)
	except KeyboardInterrupt:
		return

if __name__ == '__main__':
	main()

