#The Fizz Buzz Test
#The Fizz Buzz test is a poplular interview question used to 'help filter out the 99.5% of programming job candidates who can't seem to program their way out of a wet paper bag.'

#Write a program that returns a list of all the numbers from 1 to an interger argument. But for multiples of three use “Fizz” instead of the number and for the multiples of five use “Buzz”. For numbers which are multiples of both three and five use “FizzBuzz”
#Notes
#Make sure to return a list
def fizzBuzz(num):
    l=[]
    for i in range(1,num+1):
        if i%3==0 and i%5==0:l.append('FizzBuzz')
        elif i%3==0:l.append('Fizz')
        elif i%5==0:l.append('Buzz')
        else:l.append(i)
    return l

print(fizzBuzz(10) )
#➞ [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']

print(fizzBuzz(15) )
#➞ [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
#Notes
#Make sure to return a list