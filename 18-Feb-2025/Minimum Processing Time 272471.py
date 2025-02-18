# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: list[int], tasks: list[int]) -> int:
        processorTime.sort()  
        tasks.sort(reverse=True)  
        
        min_time = 0
        for i in range(len(processorTime)):
            task_group = tasks[i * 4:(i + 1) * 4]  
            min_time = max(min_time, processorTime[i] + max(task_group)) 
        
        return min_time
