# https://leetcode.com/problems/integer-to-roman/
def int_to_roman(num)
    
    roman = { 1 => "I", 5 => "V", 10 => "X", 50 => "L",
              100 => "C", 500 => "D", 1000 => "M",
              4 => "IV" , 9 => "IX", 40 => "XL" , 90 => "XC" , 400 => "CD" , 900 => "CM" }
    
    return roman[num] if roman[num] != nil
    
    @result = ""
    
    
    while num != 0
      num = place_value_result(num, roman)
    end
    
   @result
end

def place_value_result(num, roman)
    first_digit = num.to_s[0].to_i
    place_value = num.to_s.length

    if place_value == 4
          @result << roman[1000]
          num -= 1000
    elsif place_value == 3
          hundreds_value = first_digit * 100
          if roman[hundreds_value] != nil
              @result << roman[hundreds_value]
              num -= hundreds_value
          elsif hundreds_value > 100 && hundreds_value < 400
              @result << roman[100]
              num -= 100
              
          elsif hundreds_value > 500 && hundreds_value < 900
              @result << roman[500]
              num -= 500
          end
     elsif place_value == 2
         tens_value = first_digit * 10
         if  roman[tens_value] != nil
            @result << roman[tens_value]
            num -= tens_value
         elsif tens_value < 40
              @result << roman[10]
              num -= 10
         elsif tens_value > 50
              @result << roman[50]
              num -= 50
         end
      else
          ones_value = first_digit
          if roman[ones_value] != nil
              @result << roman[ones_value]
              num -= ones_value
          elsif ones_value < 4
              @result << roman[1]
              num -= 1
          elsif ones_value > 5
              @result << roman[5]
              num -= 5
          end
      end
end
