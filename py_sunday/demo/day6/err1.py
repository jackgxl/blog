try:
    print(aa)
except NameError as ne:
    aa = 2
    print("aa init.")
finally:
    print(aa)
