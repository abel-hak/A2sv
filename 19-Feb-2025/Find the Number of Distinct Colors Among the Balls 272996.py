# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/



class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        dicc = {} 
        freq = defaultdict(int)  
        res = []
        seen_count = 0 

        for index, col in queries:
            if index in dicc:
                prev_col = dicc[index]
                freq[prev_col] -= 1
                if freq[prev_col] == 0:  
                    seen_count -= 1

            dicc[index] = col
            if freq[col] == 0: 
                seen_count += 1
            freq[col] += 1  

            res.append(seen_count)

        return res
