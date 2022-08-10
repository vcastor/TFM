gg = gfortran 
objects = linear polynomial

all: $(objects)

$(objects): %: %.f90
	$(gg) -o $@.exe $<

clean:
	rm -f *.o *.exe
