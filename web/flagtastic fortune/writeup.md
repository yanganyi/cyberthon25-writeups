## observations

inspecting the website and navigating to sources we get index \
index has some javascript in a `<script>` tag \
we notice a function checkEligibility, which matches a precomputed hash with the correct values against a hash computed with our values \
obviously this is not bruteforceable, so we need to look harder \
we see that if it validates it sends out a fetch request to an api endpoint

## attack vector

literally just send the api request urself

## flag

`Cyberthon{fr33_fl4g_g1v34w4y_sc4m_s1t3_1s_4_sc4m}`