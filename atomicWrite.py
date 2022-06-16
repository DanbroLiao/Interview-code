from atomicwrites import atomic_write

def auto_writing(func):
    def wrapTheFunction(something):
        with atomic_write('test.txt', overwrite = True) as f:
            f.write(something)
        return func
    return wrapTheFunction

@auto_writing
def writing(something):
    print("writing {}!".format(something))

if __name__ == '__main__':
   content = input("Please enter:")
   writing(input("Please enter:"))