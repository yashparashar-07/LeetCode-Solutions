class Solution(object):
    def detectCycle(self, head):
        temp = head
        my_set = set()

        while temp is not None:
            if temp in my_set:
                return temp

            my_set.add(temp)
            temp = temp.next

        return None

obj=Solution()
obj.detectCycle