def translate(from_letters, to_letters, text):
    """
    The translate function does a letter to letter translation.
    The from_letters and to_letters parameters are expected to
    be strings of uppercase letters and both strings need to be 
    the same length. The from_letters and to_letters strings define
    a mapping such that from_letters[i] found in the text string 
    parameter will be converted to to_letters[i].  All characters in 
    the text parameter not found in from_letters are left as-is.
    Case of letters in the text parameter are preserved in the result.
    For example translate("ABC","CAB","C3PO-aBA") will return the 
    string "B3PO-cAC".  Likewise, translate("CAB","ABC","B3PO-cAC")
    will return the string "C3PO-aBA".   
    """
    # Check that parameters meet assumptions. The only assumption not
    # tested is that each character in from_letters should occur once.
    # Students should not change this code.  It is here to catch mistakes.
    if not(from_letters.isupper() and from_letters.isalpha() and 
           to_letters.isupper() and to_letters.isalpha()):
        raise ValueError("from_letters and to_letters must be all uppercase letters")
    if len(from_letters) != len(to_letters):
        raise ValueError("from_letters and to_letters must be the same length")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ''
    for i in range(len(text)):         
            index=from_letters.find(text[i])
            if index!=-1:
                result=result + to_letters[index]
            elif str.isalpha(text[i]):
                 char=from_letters.find(str.upper(text[i]))
                 result=result + str.lower(to_letters[char])
            else:
                    result=result+text[i]
    return(result)


def assign():
   file=open("commands.txt", "r")
   key_file=file.readline().strip()
   process=file.readline().strip()
   input_file=file.readline().strip()
   output_file=file.readline().strip()
   file.close()
   
   key_file_content=open(key_file,'r')
   key = key_file_content.readline()
   key_file.close()

   input_content=''
   input_file_content=open(input_file,'r')
   line = input_file_content.read()
   while line!="":
        input_content=input_content+line
        line=input_file_content.readline()
   input_file.close()


   store=[key,process,input_content,output_file]
   return(store)

def main():
   alphabet ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   [key,process,input_content,output_file]=assign()

   if process=='decrypt':
        result=translate(key,alphabet,input_content)

   if process=='encrypt':
        result=translate(alphabet,key,input_content)
   outfile=open(output_file,'r')
   outfile.write(result)
   outfile.close()

if __name__ == "__main__":
    main()