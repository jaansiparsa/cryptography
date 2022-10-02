Introduction

Cryptography is the art of changing information in such a way that the average person will not be able to understand it, but whoever is meant to receive the information can reverse the changes and make it understandable.  Ciphers and codes have been used for millennia to hide secrets by both private individuals and powerful governments, and many major historical events have hinged on how effective those ciphers were at hiding information.

A Vigenère cipher (named after a famous French cryptographer) uses a keyword to determine how to replace letters in the original message (the “plaintext”) to create the encrypted message (the “ciphertext”).  To use the Vigenère cipher, the first letter of the keyword is used to encrypt the first letter of the message.  The keyword letter is the start of a “cipher” alphabet, the same as the normal English alphabet, but shifted over to account for the new starting letter.  The plaintext letter is then replaced with the corresponding letter in the cipher alphabet.  The second letter of the keyword is then used to encode the second letter of the plaintext, and so on; when you run out of letters in the keyword, you start with the first keyword letter again.  If you encounter a space, just transfer it to the encoded message – only letters need to be encoded.

Let’s use “CODE” as an example keyword and “DUNBAR” as a sample plaintext message.  First, we need to build cipher alphabets for each letter in our keyword:
Cipher Example 
A 	B 	C 	D 	E 	F 	G 	H 	I 	J 	K 	L 	M 	N 	O 	P 	Q 	R 	S 	T 	U 	V 	W 	X 	Y 	Z
C 	D 	E 	F 	G 	H 	I 	J 	K 	L 	M 	N 	O 	P 	Q 	R 	S 	T 	U 	V 	W 	X 	Y 	Z 	A 	B
O 	P 	Q 	R 	S 	T 	U 	V 	W 	X 	Y 	Z 	A 	B 	C 	D 	E 	F 	G 	H 	I 	J 	K 	L 	M 	N
D 	E 	F 	G 	H 	I 	J 	K 	L 	M 	N 	O 	P 	Q 	R 	S 	T 	U 	V 	W 	X 	Y 	Z 	A 	B 	C
E 	F 	G 	H 	I 	J 	K 	L 	M 	N 	O 	P 	Q 	R 	S 	T 	U 	V 	W 	X 	Y 	Z 	A 	B 	C 	D
C 	D 	E 	F 	G 	H 	I 	J 	K 	L 	M 	N 	O 	P 	Q 	R 	S 	T 	U 	V 	W 	X 	Y 	Z 	A 	B
O 	P 	Q 	R 	S 	T 	U 	V 	W 	X 	Y 	Z 	A 	B 	C 	D 	E 	F 	G 	H 	I 	J 	K 	L 	M 	N

Now that we have our cipher alphabets, we can start to encrypt our message.  The first letter in the message is D. D is the 4th letter of the alphabet, so we need to replace it with the 4th letter in our first cipher alphabet, F.  The next letter is U (21st), and uses our second cipher alphabet, to be replaced with I.  We then encrypt N using the third alphabet (getting Q), and B with the fourth alphabet (getting F).  Our keyword was only four letters long, so for the fifth letter in our message, we go back to the first cipher alphabet, and replace A with C. Finally R is replaced with F and our cipher is complete.

The final product of the encryption is:

Original: DUNBAR

Encrypted: FIQFCF
Program

Create a new Python file named Encode_LastName. Where "LastName" is replaced by your last name. Important: The first letter of "encode" should be capitalized along with the first letter of your last name. The rest of the file name should be lowercase. Example: Encode_Funderburk. If you have more than one last name, use the first one that shows up in Focus.

Create a fixed variable at the top called LASTNAME and set it equal to your last name.

Students must create a function, encode(msg, key), that accepts two parameters, msg, which will be the plain text message that gets encrypted and key which is the word used to encrypt the message. The function must return the plain text message encoded as a string. Any spaces in the plain text should also appear in the encoded text. You may assume numbers and symbols will not be present.