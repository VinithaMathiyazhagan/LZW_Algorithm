#Name : Vinitha Mathiyazhagan
#Student ID: 801167041
#Email ID: vmathiya@uncc.edu


#Taking the ASCII input file and bit length as a command line argument

import sys

inputFile,N = sys.argv[1:]

#Opening and Reading the input data from the input file and storing the data in a data variable "inputdata"

with open(inputFile,"r") as f:
    inputdata = f.readline().strip()

#Defining the maximum table size where N is given as a command line argument
#Building and initilizing a dictionary where in a key:value pair - 'keys' are the charachters and the 'values' are the ascii values of those charachters
    
maximum_table_size = 2**int(N)
encodings = []                                                    #An array for storing the encoded data
dictionary = {chr(values): values for values in range(0,256)}

#Iterating through the sequence of input symbols and applying LZW compression algorithm

string = "" 
for symbol in inputdata:
    string_and_symbol= string + symbol
    if string_and_symbol in dictionary:
        string = string_and_symbol

    else:
        encodings.append(dictionary[string])
        if (len(dictionary) <=  maximum_table_size):
            dictionary[string_and_symbol] = len(dictionary)
        string = symbol

encodings.append(dictionary[string])

#Iterating through the compressed codes and converting it to 2 bytes

encodings = [ chr(code).encode('utf-16-be') for code in encodings  ]


#Changing the output filename using specific format as mentioned

output_file = inputFile.split(".")[0] + '.lzw'


#Writing the encoded data in the output file

with open(output_file,"wb") as f:
    for encoding in encodings:
        f.write(encoding)
















