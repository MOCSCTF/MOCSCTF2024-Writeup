# Writeup

Question: Long Long Long Query

1. Extracting DNS queries

tshark -r DNS_exfli.pcap -T fields -e dns.qry.name -Y "dns.flags.response == 0" | uniq -c

```
      2 89504E470D0A1A0A0000000D49484452000001260000012608.dns.com
      2 06000000CFC43DDA000000017352474200AECE1CE900000050.dns.com
      2 655849664D4D002A0000000800020112000300000001000100.dns.com
      ....
```

2. From the first few charaters in hex format, it looks like png file.

3. Remove all space from all DNS repsonse, then paste the text with hex format on 101 Editor.
```
89504E470D0A1A0A0000000D4948445200000126000001260806000000CFC43DDA000000017352474200AECE1CE900000050655849664D4D002A0000000800020112000300000001000100...
```

4. Save as png file and open the file. The flag is mentioned on the image.
> MOCSCTF{1mag3_exfli_beh!n3_DN$}
