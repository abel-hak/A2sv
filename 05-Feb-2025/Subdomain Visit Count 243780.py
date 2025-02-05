# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dicc = {}

        for i in cpdomains:
            parts = i.split(" ")
            value = int(parts[0]) 
            kke = parts[1].split(".")

            subdomains = []
            if len(kke) == 3:
                re = ".".join(kke[-2:])  
                de = kke[-1]
                subdomains = [parts[1], re, de]  
            elif len(kke) == 2:
                de = kke[-1]
                subdomains = [parts[1], de]  
            elif len(kke) == 1:
                subdomains = [parts[1]]  

           
            for sub in subdomains:
                dicc[sub] = dicc.get(sub, 0) + value

        
        return [f"{count} {domain}" for domain, count in dicc.items()]
