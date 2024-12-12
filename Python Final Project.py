Saul Resendiz
12/11/2024


			 Exam: Final Programming Project

	
	QUESTION 1.)

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
    # SETTERS   
    def set_width(self, width):
        self.__width = width 
        
    def set_height(self, height):
        self.__height = height
        
    # GETTERS 
    def get_height(self):
        return self.__height
        
    def get_width(self):
        return self.__width
        
    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)
        
    def calculate_area(self):
        return self.__height * self.__width
        
    def display(self):
        # DISPLAYING RECTANGLES' WIDTH, HEIGHT, AREA, AND PERIMETER 
        print('RECTANGLE PROPERTIES:')
        print(f'Rectangle Width: {self.__get_width()}')
        print(f'Rectangle Height: {self.__get_height()}')
        print(f'Rectangle Area: {self.__calculate_area()}')
        print(f'Rectangle Perimeter: {self.__calculate_perimeter()}')

# MAIN, SAMPLE RUN 
if __name__ == "__main__":
    rect = Rectangle(5, 10)
    rect.display()


	QUESTION 2.)

def count_frequencies(string_word_appearences):
    # create/initialize dictionary to store frequency of a word
    word_occurences = {}
    
    # LOOPING THRU EACH WORD, CHECKING THE WORDS OCCURENCES
    for x in string_word_appearences:
        # If the word is already in, add one to occurence counter
        if x in word_occurences:
            word_occurences[x] += 1
        else:
            # If not in dictionary ALREADY then set occurencee counter to 1
            word_occurences[x] = 1
    
    return word_occurences
    
input_strings = ["apple", "banana", "apple", "orange", "banana", "ROCK"]

frequency_count = count_frequencies(input_strings)

print("Frequency Count:", frequency_count)
