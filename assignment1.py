"""
### Name:
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""


def length_time():
  unit=["year", "month","day"]
  while True:
    choice=int(input("Enter a number from 1-3 to define the length of time\n 1=years 2=months 3=days: "))
    if choice==1:
      years=float(input("Enter the years of investment: "))
      return years
    elif choice==2:
      months=float(input("Enter the months of investment: "))
      return months/12
    elif choice==3:
      days=float(input("Enter the days of investment: "))
      return days/365
    else:
      print("Please enter a valid number.")


def main():
  while True:
    p=float(input("Enter the initial investment amount: "))
    rate_percentage=float(input("Enter the percentage of annual interest rate: "))
    r=rate_percentage/100
    t=length_time()
    I = p*r*t
    I=float(I)
    print(f"The simple interest is $ {I}")

if __name__ =="__main__":
  main()