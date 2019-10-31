import datetime
def main():
    dob=input('Your date of birth is: ')
    dob= int(dob)
    YearNow= datetime.datetime.now().year
    Age= YearNow-dob
    print('You have {} years old'.format(Age))

if __name__=='__main__':main()