import pymssql


class Database:
    __connection = None

    @classmethod
    def __connect(cls):
        """
        Connects to pymssql database
        :return: none
        """
        if cls.__connection is None:
            cls.__connection = pymssql.connect(server='cisdbss.pcc.edu', user='', password='',
                                               database='NAMES')


    @classmethod
    def retrieveNames(cls, Name, Gender):
        """
        Retrieves data from database according to name and gender
        :param Name: string, name input to search database for
        :param Gender: string, gender M or F to search database for
        :return: namesList, List of data retrieved from database
        """
        namesList = []

        if (cls.__connection is None):
            cls.__connect()

        myCursor = cls.__connection.cursor()
        myCursor.execute(
            "SELECT top 100 * From all_data WHERE Name=%s AND Gender=%s",
            (Name, Gender))


        namesList = myCursor.fetchall()

        return namesList












