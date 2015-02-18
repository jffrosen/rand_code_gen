#!/usr/bin/python
import sys
import random

insts = ["+", "-", "*", ">>"];
operands = ["var0", "var1", "var2", "var3", "var4"]
N_INSTS = len(insts)
N_OPDS = len(operands)

def initialize():
	print "unsigned long long trav_ctr = 0;"
	for o in operands:
		print "long long %s = %d;" % (o, random.randint(0, 1000))

	print ""

def print_label(block_num):
	print "B%d:" % block_num

def print_inc_block_ctr():
	print "trav_ctr++;"

def print_jump(num_blocks, total_travs):
	target = random.randint(0, num_blocks - 1)
	print "if (trav_ctr == %d)	goto Exit;" % total_travs
	print "else goto B%d;" % target

def print_one_inst():
	inst1_idx = random.randint(0, N_INSTS - 1)
	inst2_idx = random.randint(0, N_INSTS - 1)
	source1_idx = random.randint(0, N_OPDS - 1)
	source2_idx = random.randint(0, N_OPDS - 1)
	dest_idx = random.randint(0, N_OPDS - 1)

	if (random.randint(1,10) % 2):
		print "%s %s= %s %s %s;" % (operands[dest_idx], 
															  insts[inst1_idx],
																operands[source1_idx],
																insts[inst2_idx], 
																operands[source2_idx])
	else:
		print "%s %s= %s;" % (operands[dest_idx], 
													insts[inst1_idx],
													operands[source1_idx])
	
def print_exit_block():
	print "Exit:"
	print "return 0;"

def generate_block(blocksize_in_insts, total_blocks, block_num, total_travs):
	# block label
	print_label(block_num)

	# increment the traversed block counter
	print_inc_block_ctr()

	for i in range(0, blocksize_in_insts):
		print_one_inst()		

	# check for exit condition
	print_jump(total_blocks, total_travs)

def generate_program(blocksize_in_insts, total_blocks, n_jumps):
	# initialize traversed block counter
	initialize()

	for i in range(0, total_blocks):
		generate_block(blocksize_in_insts, total_blocks, i, n_jumps)

	# exit block
	print_exit_block()

def main(argv):
	print "int main() {"
	generate_program(20, 5000, 100000000)
	print "}"

if __name__ == "__main__":
  main(sys.argv)
