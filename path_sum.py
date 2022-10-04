class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        #going to split it in two sides, LHS and RHS 
    
        #LHS 
        tracker = 0 
        pos = root
        #while the tracker is less than the target, go left 
        while tracker < targetSum: 
            tracker += pos.left.val
            pos = pos.left #repostion where our start is each time 
            if tracker == targetSum:
                return True
        
        #if more tracker go up and move right 
        if tracker > targetSum:
            tracker -= pos.val
            while tracker < targetSum: 
                tracker += pos.right.val
                pos = pos.right #repostion tracker 
                if tracker == targetSum:
                    return True 

        #RHS 
        else:
            pos = root.val 
            while tracker < targetSum: 
                tracker += pos.right.val
                pos = pos.right #repostion where our start is each time 
                if tracker == targetSum:
                    return True
            #if more tracker go up and move right 
            if tracker > targetSum:
                tracker -= pos.val
                while tracker < targetSum: 
                    tracker += pos.left.val
                    pos = pos.left #repostion tracker 
                    if tracker == targetSum:
                        return True  

        return False

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

S = Solution()
print(S.hasPathSum(root,0))