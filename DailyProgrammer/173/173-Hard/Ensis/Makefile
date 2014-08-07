NAME=		hard

RM=		@rm -f

CXX=		g++

SRC=		src/main.cpp		\
		src/Map.cpp		\
		src/Interface.cpp

OBJ=		$(SRC:.cpp=.o)

CXXFLAGS=	-I include/

LIB=		-lsfml-graphics		\
		-lsfml-window		\
		-lsfml-system		\
		-lm

all: $(NAME)

$(NAME): $(OBJ)
	$(CXX) -o $(NAME) $(OBJ) $(LIB)

clean:
	$(RM) $(OBJ)

fclean: clean
	$(RM) $(NAME)

re: fclean all
