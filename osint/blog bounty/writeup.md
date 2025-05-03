## observations

theres one name so of course we use it

## attack vector

force search the string aka \
`"Imano Trealperson"` \
on Google

we get the url https://flaghunt.ing/ \
since the description says "he hosts a number of websites on his personal domain besides his blog" \
wait - what blog? \
we can use a site like https://crt.sh/ \
this allows us to find the link https://pwndiary.flaghunt.ing \
we see one blog post, `CTF for Beginners` \
clicking into it, we find the flag

edit: its been mentioned that for some people the force search doesnt work, an alternative path would be to search on twitter (or rather, X) which would yield https://x.com/imanotrp which points to the https://flaghunt.ing/ link either way

## flag

`Cyberthon{W0W_Y0U_F0UND_MY_BL0G_4ND_FL4G_4M4Z1NG_J0B}`