from Database import Database

class Names:
  __name = ""
  __gender = ""
  __year = 0
  __births = 0


  def __init__(self, n, g, y, b):
    self.__name = n
    self.__gender = g
    self.__year = y
    self.__births = b


  def __str__(self):
    """
    Creates a string of the parameters of the class
    :return: string, "There were (BIRTHS) births of gender (GENDER) named (NAME) in (YEAR)"
    """
    return "There were " + str(self.__births) + " births of gender " + str(self.__gender) + " named " + str(self.__name) + " in " + str(self.__year)

  @property
  def name(self):
    return self.__name

  @property
  def gender(self):
    return self.__gender

  @property
  def year(self):
    return self.__year

  @property
  def births(self):
    return self.__births

  @name.setter
  def name(self, n):
    self.__name = n

  @gender.setter
  def gender(self, g):
    self.__gender = g

  @year.setter
  def year(self, y):
    self.__year = y

  @births.setter
  def births(self, b):
    self.__births = b

  @staticmethod
  def getNames(name, gender):
    """
    Retrieves list from database according to name and gender choice entered
    and places into dictionary.
    :param name: string, name to be searched for
    :param gender: string, M or F, gender to be searched for
    :return: namesList, dictionary of objects
    """
    namesList = []
    
    namesData = Database.retrieveNames(name, gender)

    for i in namesData:
      entry = Names(i[4],i[8],i[7],i[2])
      namesList.append(entry)
    return namesList

  def getName(prompt="Please enter a name: "):
    """
    Function to prompt for and return a name.
    An empty string is invalid input and returns an error message.
    :return: string, Non-empty string of characters
    """
    name = ""
    while True:
        name = input(prompt)
        if name != "":
            return name
        else:
            print("Invalid entry. Please enter a name to search the database for.")
  
  def getGender(prompt="Please enter a gender (M/F): "):
    """
    Function to prompt for an entry of M or F.
    Any other input is invalid and returns an error message.
    :return: gender, string, M or F
    """
    gender = ""
    gender = input(prompt)
    if gender.lower() != "m" and gender.lower() != "f":
      print("Invalid response, please enter either M or F.")
    else:
      return gender