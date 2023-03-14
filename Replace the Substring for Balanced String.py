class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        q, w, e, r = count["Q"], count["W"], count["E"], count["R"]
        length = len(s)/4
        if q==w and q==e and q==r and q==length:
           return 0
        rq, rw, re, rr = 0, 0, 0, 0
        c = []
        if q > length:
            rq = q - length
            c.append("Q")
        if w > length:
            rw = w - length
            c.append("W")
        if e > length:
            re = e - length
            c.append("E")
        if r > length:
            rr = r - length
            c.append("R")
        
        cq, cw, ce, cr = 0, 0, 0, 0
        minLen = len(s)+1
        right = 0
        while s[right] not in c:
            right += 1
        left = right
        while right < len(s):
            if s[right] == "Q":
                cq += 1
            elif s[right] == "W":
                cw += 1
            elif s[right] == "E":
                ce += 1
            else:
                cr += 1
            
            while ( ("Q" in c and cq >= rq) or ("Q" not in c)) and (("W" in c and cw >= rw) or ("W" not in c)) and (("E" in c and ce >= re) or ("E" not in c)) and (( "R" in c and cr >= rr) or ("R" not in c)):
                minLen = min(minLen, right - left + 1)
                if s[left] == "Q":
                    cq -= 1
                elif s[left] == "W":
                    cw -= 1
                elif s[left] == "E":
                    ce -= 1
                else:
                    cr -= 1
                left += 1
            right += 1
        return minLen
                
               
        
