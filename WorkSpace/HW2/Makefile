CC=icc
CFLAGS=-Iinc -Wall -xHost -openmp -vec-report2 -O3

#matrix_multiply : matrix_multiply.c
#	$(CC) -o $@ $< $(CFLAGS)

matrix_multiply_parallel : matrix_multiply_parallel.c
	$(CC) -o $@ $< $(CFLAGS)

generate_rand_matrix : generate_rand_matrix.c
	$(CC) -o $@ $< $(CFLAGS)

.PHONY: clean

clean :
	rm matrix_multiply
	rm matrix_multiply_parallel
