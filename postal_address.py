#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program outputs the mailing address in proper format

def strt_address(street_number, street_name, apartment_number=None):
    # this function returns the street address

    # process
    address = street_number + " " + street_name
    if apartment_number is not None:
        address = apartment_number + "-" + address

    return address


def main():
    # this function receives input and call other function

    # input
    name = input("Enter your full name: ")
    question = input("Do you live in an apartment (Y/N)?: ")
    if question.upper() == "Y" or question.upper() == "YES":
        apartment_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name: ")
    city = input("Enter your city: ")
    province = input("Enter your province (abbreviation): ")
    postal_code = input("Enter your postal code: ")

    # output & call function
    print("")
    print(name.upper())
    if question.upper() == "Y" or question.upper() == "YES":
        address = strt_address(street_number, street_name, apartment_number)
    else:
        address = strt_address(street_number, street_name)
    print(address.upper())
    print("{0} {1}  {2}".format(
          city.upper(), province.upper(), postal_code.upper()))
    print("\nDone.")


if __name__ == "__main__":
    main()
