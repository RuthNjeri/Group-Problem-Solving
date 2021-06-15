# https://leetcode.com/problems/valid-palindrome/

def is_palindrome(s)

  valid_string = ""

  for char in 0...s.length
      if s[char].match?(/[A-Za-z0-9]/)
          valid_string << s[char].downcase
      end
  end

  start = 0
  stop = valid_string.length - 1
  while start < stop
      return false if valid_string[start] != valid_string[stop]
      start += 1
      stop -= 1
  end
  true
end