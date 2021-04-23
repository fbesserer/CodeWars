from datetime import datetime
# So let us implement the following helper which will have 2 methods:
#
#     one which verifies that the string is a valid Mongo ID string, and
#     one which finds the timestamp from a MongoID string
# If you take a close look at a Codewars URL, you will notice each kata's id (the XXX in http://www.codewars.com/dojo/katas/XXX/train/javascript)
# is really similar to MongoDB's ids, which brings us to the conjecture that this is the database powering Codewars.

class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        """returns True if s is a valid MongoID; otherwise False"""
        try:
            int(s,16)
            return False if len(s) != 24 or s != s.lower() else True
        except:
            return False

    @classmethod
    def get_timestamp(cls, s):
        """if s is a MongoID, returns a datetime object for the timestamp; otherwise False"""
        return datetime.fromtimestamp(int(s[:8], 16)) if cls.is_valid(s) is True else False


print(Mongo.is_valid('507f1f77bcf86cd79943901'))  # , False)
print(Mongo.is_valid('507f1f77bcf86cd799439016'))  # , True)
print(Mongo.is_valid('507f1f77bcf86cz799439016'))  # , False)
print(Mongo.get_timestamp('507f1f77bcf86cd79943901'))  # , False)
print(Mongo.get_timestamp('507f1f77bcf86cd799439016'))  # , datetime(2012, 10, 17, 21, 13, 27))
print(Mongo.is_valid(111111111111111111111111)) # False
Mongo.is_valid('507f1f77bcf86cD799439011') # False