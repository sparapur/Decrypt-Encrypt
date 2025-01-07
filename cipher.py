def translate(from_letters, to_letters, text):
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
                result+= to_letters[index]
            elif str.isalpha(text[i]):
                 char=from_letters.find(str.upper(text[i]))
                 result+= str.lower(to_letters[char])
            else:
                    result=result+text[i]
    return(result)


def assign():
   file=open("commands.txt", "r")
   key_file=file.readline().strip()
   process=str(file.readline().strip())
   input_file=file.readline().strip()
   output_file=file.readline().strip()
   file.close()
   
   key_file_content=open(key_file,'r')
   key = key_file_content.readline()
   key_file_content.close()

   input_content=''
   input_file_content=open(input_file,'r')
   line = input_file_content.read()
   while line!="":
        input_content=input_content+line
        line=input_file_content.readline()
   input_file_content.close()


   store=[key,process,input_content,output_file]
   return(store)

def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    [key, process, input_content, output_file] = assign()

    if process == 'encrypt':
        result = translate(alphabet, key, input_content)
    elif process == 'decrypt':
        result = translate(key, alphabet, input_content)
    else:
        raise ValueError(f"Invalid process: {process}. Expected 'encrypt' or 'decrypt'.")

    outfile=open(output_file,'w')
    outfile.write(result)
    outfile.close()

if __name__ == "__main__":
    main()