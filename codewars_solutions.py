#Even or Odd
def even_or_odd(number):
    
    if number%2 == 0:
        return ("Even")
    else:
        return ("Odd")
    pass
input_number = int(input("Enter a number to determine if even or odd: "))
result = even_or_odd(input_number)
print(f"The number {input_number} is {result}.")

#Conver a Number to a String
def number_to_string(num):
    return str(num)
input_num = float(input("Enter a number to convert it into a string: "))
result_str = number_to_string(input_num)
print(f"The string representation of the number is: '{result_str}'")

#Remove spaces from string
def no_space(x):
    return x.replace(" ", "")
input_str = input("Enter a string with spaces to remove them: ")
result_no_space = no_space(input_str)
print(f"The string without spaces is: '{result_no_space}'")

#Count vowels in a string
def get_count(sentence):
    vowels = 'aeiou'
    count = 0
    for char in sentence:
        if char in vowels:
            count+=1
    return count
input_sentence = input("Enter a sentence to count the vowels: ")
vowel_count = get_count(input_sentence)
print(f"The number of vowels in the sentence is: {vowel_count}")