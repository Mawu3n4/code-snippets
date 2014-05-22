NAME	=	flake

ML	=	flake.ml

OCAMLFLAGS =	-w A

CMX = $(ML:.ml=.cmx)

RM	=	rm -rf

################################################################################
################################################################################


all: $(NAME)

$(NAME): $(CMX)
	ocamlopt -o $@ $^

.ml.cmx:
	ocamlopt -c $< $(OCAMLFLAGS)

clean:
	$(RM) $(CMX) *.cm* *.o

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: byte clean fclean re
.SUFFIXES: .ml .cmx
