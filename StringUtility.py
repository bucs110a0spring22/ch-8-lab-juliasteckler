class StringUtility:
  def __init__(self, my_string):
    self.my_string = my_string
    
  def __str__(self):
    return self.my_string

  def vowels(self):
    count=0
    vowels = "aeiou"
    for i in self.my_string:
      if i in vowels: 
        count += 1
    if count >= 5:
      return "many"
    return str(count)

  def bothEnds(self):
    if len(self.my_string)>=2:
      return(self.my_string[0:2] + self.my_string[-2] + self.my_string[-1])
    if len(self.my_string)<=2:
      return str()

  def fixStart(self):
    start = ""
    if len(self.my_string)<=1:
      return self.my_string
    else:
      a = 0
      first_char = self.my_string[0]
      for i in self.my_string:
        if i == first_char and a != 0:
          start = start + "*"
        else:
          start = start + i 
        a = a + 1
      return start

  def asciiSum(self):
    a = 0
    for i in self.my_string:
      a = a + ord(i)
    return a 

  def cipher(self):
    empty = ""
    extraEmpty = " "
    alpha = "abcdefghigklmnopqrstuvwxyz"
    for i in self.my_string:
      if i in alpha.lower():
        b = chr(((ord(i) + len(self.my_string)) % 26))
        empty += b
      elif i in alpha.upper():
        b = chr(((ord(i) + len(self.my_string)) % 26))
        empty += b
      elif i in extraEmpty:
        empty += i
    return empty
    

    
      
    
      




      





    






