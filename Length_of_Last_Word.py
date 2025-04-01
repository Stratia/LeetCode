
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Last Word Parameter:
         - Space Behind it
         - No Letters in front of it
        Loop through string, and when a non-space item is found 
        add it to a list, this will be done by combining each string 
        into a letter, and when process is set to false it will pop 
        the string variable into the list, and set the string to None


        when letter is encountered process var will
        be set to true, to signify a word has been encountered, 
        when a space is encountered process will be set to false.
        Summary:
        
        Variables
        String_var = None
        Word_Container = []

        - Loop through string
          if letter:
            String_var+letter
          else:
              Word_Container.pop(String_var)
              String_var = None
              continue
        """
        String_var = ""
        Word_Container = []
        for letter in s:
          if " " not in letter:
            print(f"Found Letter: {letter}")
            String_var = String_var + letter
          else:
              if String_var != "": # if not blank
                print(f"Final String Var: {String_var}")
                Word_Container.append(String_var)
                String_var = ""
                continue
        if String_var != "":
           print(f"String Var Not Blank: {String_var}")  
           Word_Container.append(String_var) 
        return Word_Container[-1]

string_1 = "Hello World"
string_2 = "   fly me   to   the moon  "
string_3 = "luffy is still joyboy"
obj = Solution()
out = obj.lengthOfLastWord(string_1)

print(out)