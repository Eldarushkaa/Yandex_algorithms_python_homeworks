def search_insert(nums: list[int], target: int) -> int:
    if nums[0] > target:
        return 0
    if nums[-1] < target:
        return len(nums)
    left = 0
    right = len(nums) - 1
    while left <= right:
        cur = (left + right) // 2
        if nums[cur] == target:
            return cur
        elif nums[cur] < target < nums[cur + 1]:
            return cur + 1
        elif nums[cur] < target:
            left = cur + 1
        elif nums[cur + 1] > target:
            right = cur - 1


def length_of_lis(nums: list[int]) -> int:
    ans = [nums[0]]
    for x in nums[1:]:
        if x > ans[-1]:
            ans.append(x)
        else:
            ans[search_insert(ans, x)] = x
    return len(ans)


# seq_origin = map(int, input().split())
# seq_tokenized = map(int, input().split())
print(length_of_lis([1, 3,9,2]))
