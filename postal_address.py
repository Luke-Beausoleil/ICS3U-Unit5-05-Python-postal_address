#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program outputs the mailing address in proper format


def strt_address(name, street_number, street_name, city, province,
                 postal_code, apartment_number=None):
    # this function returns the street address

    # process
    if apartment_number is not None:
        address = "{0}\n{6}-{1} {2}\n{3} {4}  {5}".format(name.upper(),
                                                          street_number,
                                                          street_name.upper(),
                                                          city.upper(),
                                                          province.upper(),
                                                          postal_code.upper(),
                                                          apartment_number)
    else:
        address = "{0}\n{1} {2}\n{3} {4}  {5}".format(name.upper(),
                                                      street_number,
                                                      street_name.upper(),
                                                      city.upper(),
                                                      province.upper(),
                                                      postal_code.upper())

    return address


def main():
    # this function receives input and call other function

    # input
    try:
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
        if question.upper() == "Y" or question.upper() == "YES":
            address = strt_address(name, street_number, street_name, city,
                                   province, postal_code, apartment_number)
        else:
            strt_address(name, street_number, street_name, city, province,
                         postal_code)
        print("{0}\n\nDone.".format(address))
    except(Exception):
        print("Invalid Input\nDone.")


if __name__ == "__main__":
    main()
