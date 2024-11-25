import sys


def main():
  args = sys.argv #コマンドラインの受け取り

  try:
    print(args)
    if args[1]=="reverse": #内容を逆にして返す
      try:
        inputpath = args[2]
        outputpath = args[3]
        contents = ''
        with open(inputpath) as f:
          contents = f.read()
          print(contents)
        with open(outputpath, 'w') as f:
          f.write(contents[::-1])
      except:
        print("Your path is wrong.\n")
    elif args[1]=="copy":
      try:
        inputpath = args[2]
        outputpath = args[3]
        contents = ''
        with open(inputpath) as f:
          contents = f.read()
        with open(outputpath, 'w') as f:
          f.write(contents)
      except:
        print("Your path is wrong.\n")
    elif args[1]=="duplicate-contents":
      try:
        inputpath = args[2]
        contents = ''
        with open(inputpath) as f:
          contents = f.read()
        content_duplicate = contents * int(args[3])
        with open(inputpath, 'w') as f:
          f.write(content_duplicate)
      except:
        print("Your input is wrong.\n")
    elif args[1]=="replace-string":
      try:
        inputpath = args[2]
        contents = ''
        with open(inputpath) as f:
          contents = f.read()
        contents = contents.replace(args[3], args[4])
        with open(inputpath, 'w') as f:
          f.write(contents)
      except:
        print("Your path is wrong.\n")
  except:
    print("Your input is invalid.\n")


if __name__ == '__main__':
  main()
