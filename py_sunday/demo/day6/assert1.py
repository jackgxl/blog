try:
    a = input("int number: ")
    assert a == 10,"a != 10"
    print(10/a)
except AssertionError as ae:
    print("ae")
finally:
    print("end")

