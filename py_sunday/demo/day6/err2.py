try:
#    bb = 2
    print(bb)
    print(11/0)
except ZeroDivisionError as ze:
    print("ze")
except NameError as ne:
    print("ne")
finally:
    print("end")
