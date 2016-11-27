from __future__ import division


def extended_b_lines(usage, blocking):
	'''
	Uses the Extended Erlang B formula to calcluate the ideal number of lines
	for the given usage in erlangs and the given blocking rate.

	Usage:
	extended_b_lines(usage, blocking)
	'''

	line_count = 1
	while extended_b(usage, line_count) > blocking:
		line_count += 1
	return line_count


def extended_b(usage, lines, recall=0.5):
	'''
	Usage:
	extended_b(usage, lines, recall=0.5)
	'''

	original_usage = usage
	while True:
		PB = b(usage, lines)
		magic_number_1 = (1 - PB) * usage + (1 - recall) * PB * usage
		magic_number_2 = 0.9999 * original_usage
		if magic_number_1 >= magic_number_2:
			return PB
		usage = original_usage + recall * PB * usage
	return -1


def b(usage, lines):
	'''
	Usage:
	b(usage, lines)
	'''

	if usage > 0:
		PBR = (1 + usage) / usage
		for index in range(2, lines + 1):
			PBR = index / usage * PBR + 1
			if PBR > 10000:
				return 0
		return 1 / PBR
	return 0
