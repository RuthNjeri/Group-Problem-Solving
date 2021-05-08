class Solution:
    def isPalindrome(self, s: str) -> bool:

        # remove non-alpha numeric characters from string
        s = ''.join(e for e in s if e.isalnum())

        if s == '' or len(s) == 1:
            return True
        
        # convert to lower case
        s = s.lower()
        
        # check if string is equal to its reverse
        return s == s[::-1]

# In Ruby
# First remove any character that is not alphanumeric.
# During an interview, without the knowledge of regex (.match(/[A-Za-z0-9]/)) you can create
# an array with all the letters and numbers then use .include? %w(a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0)
# Then use two pointers
# one at the start and another at the end(stop)
# if at any point the start character is not equal to the stop character, return false
# def is_palindrome(s)

#   valid_string = ""

#   for char in 0...s.length
#       if s[char].match?(/[A-Za-z0-9]/)
#           valid_string << s[char].downcase
#       end
#   end

#   start = 0
#   stop = valid_string.length - 1
#   while start < stop
#       return false if valid_string[start] != valid_string[stop]
#       start += 1
#       stop -= 1
#   end
#   true
# end