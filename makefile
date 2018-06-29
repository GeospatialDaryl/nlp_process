CXX = g++ -O2 -Wall
FILES:=$(shell ls)

all: clean code1 code2

code1: code1.cc utilities.cc
        $(CXX) $^ -o $@

code2: code2.cc utilities.cc
        $(CXX) $^ -o $@

init:
        (echo "from dict_tools import dict_tools"; echo "dictA = {}"; \
                echo "dict_tools.pickle_dict(dictA, 'dictSingles')") | python
        (echo "from dict_tools import dict_tools"; echo "dictA = {}"; \
                echo "dict_tools.pickle_dict(dictA, 'dictDuos')") | python
        (echo "from dict_tools import dict_tools"; echo "dictA = {}"; \
                echo "dict_tools.pickle_dict(dictA, 'dictTrios')") | python

clean:
        rm *.pickle
        echo Clean done

list:

        echo $(FILES)

process:
        for x in $(FILES); do splittie_d.py $$x; done
