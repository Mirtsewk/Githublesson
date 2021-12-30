#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python') 

#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('Coding' + ' ' + 'For' + ' ' + 'All')

#3. Declare a variable named company and assign it to an initial value "Coding For All".
company='Coding For All'

#4. Print the variable company using print().
print(company)

#5. Print the length of the company string using len() method and print().
print(len(company))

#6. Change all the characters to uppercase letters using upper() method.
print(company.upper()) 

#7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase()) 

#9. Cut(slice) out the first word of Coding For All string.
print(company[0:7])

#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.rfind('Coding')) 

#11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python')) 

#12. Change Python for Everyone to Python for All using the replace method or other methods.
sentence= 'Python for everyone'
print(sentence.replace('Python for everyone', 'Python for all')) 

#13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(' ')) 

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
applications ='Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(applications.split(' , ')) 

#15. What is the character at index 0 in the string Coding For All.
print(company[0])

#16. What is the last index of the string Coding For All.
print(company[-1])

#17.What character is at index 10 in "Coding For All" string.
print(company[10])

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
string = 'Python for Everyone'
words = string.split()
acronym = words [0][0] + words[1][0]

#20. Use index to determine the position of the first occurrence of C in Coding For All.

