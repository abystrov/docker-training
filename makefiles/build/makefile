CC=gcc
CFLAGS=-I.

build: hellomake.o hellofunc.o
	$(CC) -o hellomake hellomake.o hellofunc.o
clean:
	rm -f *.o 
all: up

up: hellomake
	./hellomake

.PHONY: all up
