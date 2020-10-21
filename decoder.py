#Name : Vinitha Mathiyazhagan
#Student ID: 801167041
#Email ID: vmathiya@uncc.edu


#Taking the ASCII input file and bit length as a command line argument
import sys

inputFile,N = sys.argv[1:]

#Opening and Reading the encoded data from the input file and storing it in a data variable "encodings"

with open(inputFile,"rb") as f:
    encodings=f.readline()

#Iterating through the encoded data and converting it into integers

encodings = [ord(code) for code in encodings.decode('utf-16-be')]



#Defining the maximum table size where N is given as a command line argument
#Re-building and initilizing the dictionary used in encoding where in a key:value pair - 'keys' are ascii values and the 'values' are the charachters of those ascii values

maximum_table_size = 2**int(N)
dictionary = {values:chr(values) for values in range(0,256)}
decodings =[]                                                      # Array for storing the decoded data

#Iterating through the encoded data and applying LZW decompression algorithm

string = ""
string=dictionary[ encodings[0] ]
decodings.append(string)

for code in encodings[1:]:
    if not(code in dictionary):
        new_string=string+string[0]
    else:
        new_string=dictionary[code]
    decodings.append(new_string)

    if (len(dictionary) <=  maximum_table_size):
        dictionary[len(dictionary)]=string+new_string[0]
        string=new_string

decodings = ''.join(decodings)

#Changing the output filename using specific format as mentioned

output_file = inputFile.split('.')[0]+"_decoded.txt"

#Writing the decompressed  data in the output file

with open(output_file,"w") as f:
        f.write(decodings+'\n')







