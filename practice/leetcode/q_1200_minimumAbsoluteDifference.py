# front_matter = {
#     "qid": 1200,
#     "title": "Minimum Absolute Difference",
#     "titleSlug": "minimum-absolute-difference",
#     "difficulty": "Easy",
#     "tags": ["Array", "Sorting"],

    
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
def main():
    solu = Solution()
    solu.minimumAbsDifference([40,11,26,27,-20])
    
class Solution:
    """Given an array of **distinct** integers `arr`, find all pairs of elements with the minimum absolute difference of any two elements.

    Return a list of pairs in ascending order(with respect to pairs), each pair `[a, b]` follows

    * `a, b` are from `arr`
    * `a < b`
    * `b - a` equals to the minimum absolute difference of any two elements in `arr`



    **Example 1:**

    ```
    Input: arr = [4,2,1,3]
    Output: [[1,2],[2,3],[3,4]]
    Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
    ```
    **Example 2:**

    ```
    Input: arr = [1,3,6,10,15]
    Output: [[1,3]]
    ```
    **Example 3:**

    ```
    Input: arr = [3,8,-10,23,19,-4,-14,27]
    Output: [[-14,-10],[19,23],[23,27]]
    ```


    **Constraints:**

    * `2 <= arr.length <= 10^{5}`
    * `-10^{6} <= arr[i] <= 10^{6}`
    """

    def minimumAbsDifference(self, arr):

        outcomes = []
        arr = sorted(arr)
        diff = {}

        smallest = arr[1] - arr[0]
        # print(smallest)

        
                    
        #             outcomes.append([arr[i], arr[i+1]])
        
        # print(diff)

        
        
        # outcomes.append([arr[i], arr[i+1]])
            # elif arr[i+1] - arr[i
        
         



        print(outcomes)
    




        # sums = {}
        # diff = []
        # output = set()

        # for i in range(len(arr)):
        #     for j in range(len(arr)):
        #         if arr[i] > arr[j]:
        #             diff.append((arr[i], arr[j]))
        
        # smallest = (diff[0][0], diff[0][1])
        # for i in diff:
        #     if (i[0] - i[1]) < diff[0][0] -  diff[0][1]:
        #         smallest = (i[0], i[1])
        #         output.add(smallest)
        #     else:
        #         output.add(smallest)
        
        # output = [list(i) for i in sorted(output)]
        # print(output)


        
main()
    # If you have multiple solutions, add them all here as methods of the same class.
