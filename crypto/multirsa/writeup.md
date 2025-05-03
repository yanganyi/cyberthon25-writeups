## observations

the server encrypts the flag using RSA public expo $e = 5$\
for each encryption, new $N = p * q$ and $x$ are chosen\
message is blinded: $m' = m * x$\
encryption is given as: $flagenc = (m * x) ^ e$\
the server outputs: $(flagenc, \ x,\ N)$

## attack vector

it is unimportant that e is small \
first we start by unblinding through modular inverse
$$
M_i = \frac{flagenc_i}{x^e_i} \mod \ n_i = m^e \ mod \ n_i
$$
combine $m_i$ with CRT
$$
m^e \ mod \ N \ where \ N = n_0 \times n_1 \times ... \ \times n_4\
$$
we have that
$$
m^e < N
$$
hence calculate
$$
m = \sqrt[e]{m^e}
$$

## flag

`Cyberthon{RSA_w1th_r3l4t3d_m3ss4g3s_1s_n0t_s3cur3_45908gj4590gjg}`