For decoding and obtaining the flag, the order must be dehexing, then de-xoring( or simply xor it again) and then shifting.

In dehexing, we will add two consecutive charecters as one charachter and then, these charachters are dehexed and stored into
bytearray. I converted this bytearray into string as i am more comfortable with string.

For de-xoring, de-xoring is the same as the xor operation. So we apply the same xor opperation to the string's each charechter now and store it into a list.

After de-xoring, all the charechter's ascii values are shifted according to the key given.

Finally, after converting the following list to string, Reversing is done!:)


