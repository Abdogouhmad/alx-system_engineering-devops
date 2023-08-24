# Colors
RED=\033[0;31m
GREEN=\033[0;32m
MAGENTA=\033[0;35m
NC=\033[0m # No Color

#program
program= 0-simple_web_stack.tex

# Compiler
CC= xelatex
XFLAGS= -file-line-error
BIB=bibtex
BIBpro=ts
#BUILDIR

build: $(program)
	@printf "${MAGENTA}Building...${NC}\n"
	@$(CC) $(XFLAGS) $(program) > /dev/null 2>&1
	@if [ $$? -eq 0 ]; then \
		printf "${GREEN}compiled${NC} \n"; \
	else \
		printf "${RED}Error compilation!${NC} \n"; \
	fi

clean:
	@printf "${RED}Cleaning...${NC} \n"
	@rm -f *.aux *.log *.out *.toc *.xdv *.fls *.fdb_latexmk  *.bbl *.blg  *.bcf *.xml >/dev/null 2>&1
	@if [ $$? -eq 0 ]; then \
		printf "${GREEN}Done!${NC} \n"; \
	else \
		printf "${RED}Error!${NC} \n"; \
	fi