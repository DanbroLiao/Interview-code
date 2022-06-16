from pyarrow import parquet
import json
def parquetFunction(func):
   def wrapTheFunction(list_):
      with open("test.parquet") as fo:
           for row in parquet.DictReader(fo,columns=list_):
               print(json.dumps(row))
      return func
   return wrapTheFunction

@parquetFunction
def reading(list_):
   pass

if __name__ == "__main__":
  reading(['a','b'])