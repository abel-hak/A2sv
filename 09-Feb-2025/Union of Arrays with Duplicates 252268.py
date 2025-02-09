# Problem: Union of Arrays with Duplicates - https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab


class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        seen = set()
        for i in a:
            if i not in seen:
                seen.add(i)
        for i in b:
            if i not in seen:
                seen.add(i)
                
        return len(seen)