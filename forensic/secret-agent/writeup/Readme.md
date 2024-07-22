# Writeup

Question: Do you find Secret Dot?

1. Find the path traversal (dot dot slash) attack pattern.

```
198.33.3.33 - - [09/Mar/2016:14:20:23] "GET /oldlink?file=../../invoice.pdf&JSESSIONID=SD7SL9FF10ADFF44873 HTTP 1.1" 200 3725 "http://www.exploratorystore.io/oldlink?file=../../invoice.pdf" "Mozilla/5.0 (Windows NT 6.1; TU9DU0NURnskZWNyM3RfQGdlbnR9) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5"
198.33.3.33 - - [09/Mar/2016:14:20:23] "GET /oldlink?file=../../invoice.doc%00.pdf&JSESSIONID=SD7SL9FF10ADFF44873 HTTP 1.1" 200 3725 "http://www.exploratorystore.io/oldlink?file=../../invoice.doc%00.pdf& "Mozilla/5.0 (Windows NT 6.1; TU9DU0NURnskZWNyM3RfQGdlbnR9) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5"
```

> MOCSCTF{$ecr3t_@gent}
