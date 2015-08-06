#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.

# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

def print_twice(f):
	f()
	f()

def print_four(f):
	print_twice(f)
	print_twice(f)

def print_border_start_segment():
	print '+','-','-','-','-',

def print_row_start_segment():
	print '|',' ',' ',' ',' ',

def print_border_end_segment():
	print '-','-','-','-','+'

def print_row_end_segment():
	print ' ',' ',' ',' ','|'

def print_2_empty_cols():
	print_row_start_segment()
	print '|',
	print_row_end_segment()

def print_4_empty_cols():
	print_row_start_segment()
	print_row_start_segment()
	print_row_start_segment()
	print '|',
	print_row_end_segment()

def two_by_two():
	print_border_start_segment()
	print '+',
	print_border_end_segment()
	print_four(print_2_empty_cols)
	print_border_start_segment()
	print '+',
	print_border_end_segment()
	print_four(print_2_empty_cols)
	print_border_start_segment()
	print '+',
	print_border_end_segment()


def four_by_four():
	print_four(print_border_start_segment)
	print '+'
	print_four(print_4_empty_cols)

	print_four(print_border_start_segment)
	print '+'
	print_four(print_4_empty_cols)

	print_four(print_border_start_segment)
	print '+'
	print_four(print_4_empty_cols)

	print_four(print_border_start_segment)
	print '+'
	print_four(print_4_empty_cols)

	print_four(print_border_start_segment)
	print '+'





# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    
    two_by_two()
    four_by_four()


if __name__ == "__main__":
    main()