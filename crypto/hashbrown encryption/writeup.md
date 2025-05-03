## observation

ok so we see `encrypt()` implemented but not `decrypt()`, so its our job to do so \
looking closer at the `encrypt()` function we notice that \
1. file is split into 2 byte chunks
2. if last chunk is 1 byte, add `0x20` (space)
3. salt is added infront of chunk
4. hashed using blake2s and written line by line

## attack vector

we notice that the salt is given \
hence given the small search space ($256 \times 256 = 65536$) \
we just need a lookup table

we open the encrypted file, match each line to an entry in the look up table \
concantenate the chunks and write to `hashbrown_flag.pbm.zip` \
unzip with computer
scan the given qr code with phone

## flag

`Cyberthon{l00kupt4blesftw!}`