class harshad():
    
  def __init__(self, args:int):
      """Instantiates the harshad class """
      self._number :int = args
      self.FindOfN = self.instFindOfN
      self.isHarshad = self.instisHarshad
      self._harshadarr = [1,2,3]
      if not (isinstance(self._number,int)):
        raise TypeError("Only integers are allowed!")
      if self._number <= 0 :
        raise ValueError("Value Must be higher than 0!")

  def instisHarshad(self:int) -> bool:
    """ Takes parameter number and returns a boolean value determining if it a harshad.True - The input is a harshad.False - The input is not a harshad """
    var1 = 0
    for x in str(self._number):
        var1 += int(x)
    var2 = self._number % var1 == 0
    if var2:
        return True
    elif not var2:
        return False

  def instFindOfN(self:int)->int:
    """Takes init value and uses it as n to find the nth value in the harshad sequence """
    sn = self._number - 1 # self._number -1 
    if (sn <= (len(self._harshadarr) - 1)):
        return (self._harshadarr[sn])
    else:
        startnum = self._harshadarr[-1]
        while True:
          var1 = 0
          for x in str(startnum):
              var1 += int(x)
          var2 = startnum % var1 == 0
          if var2:
              self._harshadarr.append(startnum)
              startnum += 1
          elif not var2:
              startnum += 1
          if (len(self._harshadarr) - 1) == (sn):
            return self._harshadarr[sn]

    
  @staticmethod # these static methods can do without instantiation eg harshad.isHarshad(x) instead of harshad(x).isHarshad()
  def isHarshad(number:int) -> bool:
    """ Takes parameter number and returns a boolean value determining if it a harshad.True - The input is a harshad.False - The input is not a harshad """
    var1 = 0
    for x in str(number):
        var1 += int(x)
    var2 = number % var1 == 0
    if var2:
        return True
    elif not var2:
        return False
  

  @staticmethod  # these static methods can do without instantiation 
  def FindOfN(number:int) -> int:
      """Takes init value and uses it as n to find the nth value in the harshad sequence """
      harshadarr = [1,2,3] 
      sn = number - 1 # self._number-1 
      if (sn <= (len(harshadarr) - 1)):
          return (harshadarr[sn])
      else:
          startnum = harshadarr[-1]
          while True:
            var1 = 0
            for x in str(startnum):
                var1 += int(x)
            var2 = startnum % var1 == 0
            if var2:
                harshadarr.append(startnum)
                startnum += 1
            elif not var2:
                startnum += 1
            if (len(harshadarr) - 1) == (sn):
                return harshadarr[sn]
              
