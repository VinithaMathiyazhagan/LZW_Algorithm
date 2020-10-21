### LZW ALGORITHM
STUDENT ID: 801167041
STUDENT NAME:	Vinitha Mathiyazhagan
UNCC EMAIL ID: vmathiya@uncc.edu
PROGRAMMING LANGUAGE: Python 
OS : Windows
COMPILER: Python 3.8
FILES: encoder.py and decoder.py

### ABSTRACT
The Lempel–Ziv–Welch  (LZW)  algorithm is  a  lossless  data  compression  algorithm. It takes in a file as input with the specified number of bits and encodes the input sequence of symbols into integers by grouping them into strings. And the decoder file takes in the output file with the encoded data in it, looks up the code for it in the dictionary and returns the string associated with the code using decoding algorithm.

### PROGRAM DESIGN

### Encoding/Compressing

**IMPORT MODULES:**

 - sys : For specifying the ASCII text file <inputFile.txt> and bit length N <Number of bits> as a command line argument
 
**COMMAND LINE ARGUEMNT AND READING THE INPUT FILE:**

  - The ASCII text file name and bit length is given as command line argument
  - Read the input data from the specified input file using readline()

**INITIALIZATION OF DICTIONARY:**

  - Defining the maximum table size as 2**int(N) where N is the numbers of bits given as a command line argument. It is 12 in this case which returns 4096.
  - Building and initializing the dictionary of size 256 using dictionary data structure used in python.It is basically a key - value pair.
  - For example: Dictionary = {chr(values):values}, where chr(values) are the keys(charachters) and values are the ascii values of those charachters.

**APPLYING LZW ENCODING ALGORITHM:**

  - We create a empty array encodings = [] to store the encoded data
  - Iterate through the input sequence of symbols from the input file and appends them one by one to the current string. 
  - Checks if the resulting string is in the dictionary, if so it reads in the next symbol and appends it to the current string
  - If the resulting string is not in dictionary, it adds the string without the symbol to the encodings array and adds the resulting string(string+symbol) to the dictionary with its code and resets the current string with the symbol
  - Finally, we get an array with all the encoded data in it.
  
**ENCODED OUTPUT SAVED IN 2 BYTES:**

  - Iterating through the codes in the encoded data and converting it to binary.

**WRITING ENCODED DATA IN OUTFILE FILE USING SPECIFIC FORMAT FOR THE FILENAME:**

  - Output filename - <Input  File  Name  without  extension>  +  “.lzw”
  - Writing the encoded data in the output file

### Decoding/Decompressing

**IMPORT MODULES:**
 - sys : For specifying the ASCII text file <inputFile.lzw> and bit length N <Number of bits> as a command line argument

**COMMAND LINE ARGUEMNT AND READING THE INPUT FILE:**

  - The ASCII text file name and bit length is given as command line argument
  - Read the input data from the specified input file using readline()

**CONVERSION OF BINARY INTO INTEGERS:**
  - Converting the binary into integers using the below function
  - encodings = [ord(code) for code in encodings.decode('utf-16-be')]

**REBUILDING THE DICTIONARY USED FOR ENCODING:**

  - Defining the maximum table size as 2**int(N) where N is the numbers of bits given as a command line argument. It is 12 in this case which returns 4096.
  - Re-building and initializing the dictionary of size 256 using dictionary data structure used in python.It is basically a key - value pair.
  - For example: Dictionary = {values:chr(values)}, where chr(values) are the values(charachters) and values are the ascii values of those charachters.

**APPLYING LZW DECODING ALGORITHM:**
  - We create a empty array decodings = [] to store the decoded data
  - It first reads in a input code, looks up the string associated with the code in the dictionary and adds the string to the decoding array
  - Iterates over the codes in the encoded data , if there is no such code in the dictionary, new string corresponding to this code consists of the previously decoded string with the first character of the previously decoded string is appended
  - If the code exists in the dictionary, the new concatenated code is added to the dictionary and increments the code value.

**WRITING DECODED DATA IN OUTFILE FILE USING SPECIFIC FORMAT FOR THE FILENAME:**
  - Output filename : <File Name without extension> + "_decoded.txt"
  - Writing the decoded data in the output file

**HOW TO RUN THE PROGRAM:**

  - Save the given two files encoder.py and decoder.py in the location where the input file is present
  - Open the command window.
  -Set the current directory to the location where the input file is present.
  - To encode, type: 
	python encoder.py <inputFileName.txt> <number of Bits>

  - To decode, type:
	python decoder.py <inputFileName.lzw> <number of Bits>

  - The encoded file will be saved as inputFileName.lzw

  - The decoded file will be saved as inputFileName_decoded.txt

### UNIT TESTING:

This program works well with both the examples provided on canvas.
Input file data - abbbab
Example1: **Encoded data** - [97, 98, 257, 256]
          **16-bit format**- 00000000 01100001 00000000 01100010 00000001 00000001 00000001 00000000
          **Decoded data** - abbbab

Input file data - abcabcabcabcabcabcabcabcabcabcabcabc
Example2: **Encoded data** - [97, 98, 99, 256, 258, 257, 259, 262, 261, 264, 260, 266, 263, 99]
          **16-bit format**- 00000000 01100001 00000000 01100010 00000000 01100011 00000001 00000000 00000001 00000010 00000001 00000001 00000001 00000011 00000001 00000110 00000001 00000101 00000001 00001000 00000001 00000100 00000001 00001010 00000001 00000111 00000000 01100011
          **Decoded data** - abcabcabcabcabcabcabcabcabcabcabcabc

I also tried with two more examples other than the ones that was provided on canvas and found that this algorithm works well when the data has redundancy and is sufficiently large. Below are the two mentioned examples:

Input file data - ABBABBBABBA
Example3: **Encoded data** - [65, 66, 66, 256, 257, 259, 65]
          **16-bit format**-00000000 01000001 00000000 01000010 00000000 01000010 00000001 00000000 00000001 00000001 00000001 00000011 00000000 01000001
          **Decoded data** - ABBABBBABBA
            
Input file data - bananabanana
Example4:**Encoded data** - [98, 97, 110, 257, 97, 256, 258, 258]
         **16-bit format**-00000000 01100010 00000000 01100001 00000000 01101110 00000001 00000001 00000000 01100001 00000001 00000000 00000001 00000010 00000001 00000010
         **Decoded data** - bananabanana
          

### SUMMARY:

As mentioned above, I believe that this algorithm works well when the data has redundancy and the size of the data is sufficiently large.


























