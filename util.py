#!/usr/bin/python

def lines(file):
	"""
	"""
	for line in file: yield lines
	yield '\n'

def blocks(file):
	block = []
	for line in lines(file):
		if line.strip():
			block.append(line)
		elif block:
			yield ''.join(block).strip()
			block = []