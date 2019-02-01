#!/usr/bin/env python
# -*-coding:utf-8-*-
import unittest
from collections import OrderedDict
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # resp_ = set(nums)
        from collections import OrderedDict
        resp_ = OrderedDict.fromkeys(nums).keys()
        for index,value in enumerate(resp_):
            nums[index] = value
        return len(resp_)

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        data = [0] * (len(nums))
        num_len = len(nums)
        if k > num_len:
            k = k % num_len
        for i,val in enumerate(nums):
            if  i+k < len(nums):
                data[i+k] = val
            else:
                data[i + k - num_len] = val
        for index,val in enumerate(data):
            nums[index] = val
        return nums

    def reverseBits(self, n):
        data = bin(n)
        print(data)
        list_data =list(data)
        data = list_data[2:]
        num_len = 32 - len(data)
        data = num_len * ['0'] + data
        data.reverse()
        int_data = "".join(data)
        print(int_data)
        return int(int_data,2)

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        resp_ = Counter(nums)
        if max(resp_.values()) > 1:
            return True
        else:
            return False

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import Counter
        resp_ = Counter(nums)
        for key,var in resp_.items():
            if var >1:
                start = "".join(nums).find(key)
                for row in range(var):
                    end = "".join(nums[start+k:])

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        resp_ = Counter(nums)
        val = min(resp_.values())
        if val ==1:
            for key,row in resp_.items():
                if row == 1:
                    return key

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        nums1_counter = Counter(nums1)
        nums2_counter= Counter(nums2)
        resp_ = Counter(nums1 + nums2)
        end_data  = []
        for key,val in resp_.items():
            if val > 1:
                nums1_counter.get(key)
                num_data = min(nums1_counter.get(key,0),nums2_counter.get(key,0))
                if num_data > 0:
                    end_data.extend([key] * num_data)
        return end_data

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_data = "".join(map(str,digits))
        return map(int,list(str(int(digits_data) + 1)))

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len  = len(nums)
        i = 0
        j = 0
        while True:
            if i == nums_len:
                nums.extend([0] * j)
                break
            if nums[i] == 0:
                del nums[i]
                j += 1
                nums_len -= 1
            else:
                i += 1

        return nums

    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        s.reverse()

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            flag = True
        else:
            flag = False
        data = list(str(abs(x)))
        data.reverse()
        data = "".join(data)
        data = int(data)
        if flag:
            if data > 2 **31 -1:
                return 0
        else:
            if -data < -2 **31:
                return 0
            else:
                return -data
        return data

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        data = list(s)
        from collections import Counter
        if not data:
            return -1
        data_dict = Counter(data)

        min_val = min(data_dict.values())
        min_val_list = []
        if min_val == 1:
            for key,val in data_dict.items():
                if val==1:
                    min_val_list.append(key)
        if len(min_val_list) < 1:
            return -1
        first_char = len(s)
        for row in min_val_list:
            _stmt_ = s.find(row)
            print(_stmt_)
            first_char = min(_stmt_,first_char)
        return first_char

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = list(s)
        t_list = list(t)
        import unittest
        s_list.sort()
        t_list.sort()
        if len(s_list) != len(t_list):
            return False
        for i in range(min(len(s_list),len(s_list))):
            if s_list[i] != t_list[i]:
                return False
        else:
            return True

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        data = list(s)
        end_data = filter(lambda x: x.isalnum(),data)
        list_data =map(lambda x: x.lower() ,end_data)
        list_data = [row for row in list_data]
        list_len = len(list_data)
        for i in range(int(list_len/2)):
            if list_data[i] != list_data[-i-1]:
                return False
        else:
            return True

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        data = str.lstrip()
        if len(data) ==0:
            return 0
        if len(data) >= 2:
            if data[0] in ("-","+") and data[1] in ("-","+"):
                return 0
        end_list = []
        flag = False
        if data[0].isdigit() or  data[0] in ("-","+"):
            if data[0] in ("-","+"):
                end_list.append(data[0])
                flag = True
            for row in list(data):
                if row in ("-","+") and  flag :
                    if row not in end_list:
                        break
                    continue
                elif row.isdigit():
                    end_list.append(row)
                else:
                    break
        if not end_list:
            return 0
        else:
            if len(end_list) == 1 and ("-" in end_list or "+" in end_list):
                return 0
            end_data = int("".join(end_list))
            if end_data > 0:
                if end_data > 2** 31 - 1:
                    return 2** 31 - 1
                else:
                    return end_data
            else:
                if end_data < -2** 31:
                    return -2** 31
                else:
                    return end_data

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) ==0:
            return ''
        if len(strs) == 1:
            return strs[0]

        min_len = min([len(row) for row in strs])
        min_str = [row for row in  filter(lambda x:len(x)==min_len,strs)]
        min_str_fliter = min_str[0]
        for i in range(len(min_str_fliter)):
            len_data = [row.startswith(min_str_fliter[:min_len-i]) for row in strs ]
            if False in len_data:
                continue
            else:
                return strs[0][:min_len-i]
        else:
            return ''

    def new_longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        # 在使用max和min的时候已经把字符串比较了一遍
        # 当前列表的字符串中，每个字符串从第一个字母往后比较直至出现ASCII码 最小的字符串
        s1 = min(strs)
        # 当前列表的字符串中，每个字符串从第一个字母往后比较直至出现ASCII码 最大的字符串
        s2 = max(strs)
        # 使用枚举变量s1字符串的每个字母和下标
        for i, c in enumerate(s1):
            # 比较是否相同的字符串，不相同则使用下标截取字符串
            if c != s2[i]:
                return s1[:i]
        return s1

class SolutionUnitest(unittest.TestCase):

    def setUp(self):
        self.s = Solution()
    def test_removeDuplicates(self):
        s = Solution()
        orig_data = [1,2,5,6,1]
        end_data  = [1,2,5,6]
        s.removeDuplicates(orig_data)
        self.assertEqual(len(end_data),s.removeDuplicates(orig_data))
    def test_rotate(self):
        print( self.s.rotate([1,2,3,4,5,6,7,8,9],1))
        self.assertListEqual([5,7,0,2],self.s.rotate([0,2,5,7],2))

    def test_containsDuplicate(self):
        self.assertTrue(self.s.containsDuplicate([1,2,3,1]))

    def test_plusOne(self):
        self.assertListEqual(self.s.plusOne([9,9]),[1,0,0])

    def test_moveZeroes(self):
        print(self.s.moveZeroes([0,0,0,0,1]))
        self.assertListEqual(self.s.moveZeroes([0,0,0,0,1]), [1,0,0,0,0])

    def test_firstUniqChar(self):
        self.assertEqual(self.s.firstUniqChar("aaffccgg"),-1)
        self.assertEqual(self.s.firstUniqChar("aaffcg"),4)
        self.assertEqual(self.s.firstUniqChar("aaffccg"),6)
        self.assertEqual(self.s.firstUniqChar(""), -1)

    def test_isAnagram(self):
        self.assertEqual(self.s.isAnagram("tt","tt"),True)

    def test_isPalindrome(self):
        self.assertTrue(self.s.isPalindrome("aba"))
        self.assertFalse(self.s.isPalindrome("abc"))
        self.assertTrue(self.s.isPalindrome("a"))
        self.assertTrue(self.s.isPalindrome("Aa"))

    def test_myAtoi(self):
        self.assertEqual(self.s.myAtoi('123a'),123)
        self.assertEqual(self.s.myAtoi('a123a'), 0)
        self.assertEqual(self.s.myAtoi('-123a'), -123)
        self.assertEqual(self.s.myAtoi(''), 0)
        self.assertEqual(self.s.myAtoi('++1'), 0)
        self.assertEqual(self.s.myAtoi('-'), 0)
        self.assertEqual(self.s.myAtoi('+-1'), 0)
        self.assertEqual(self.s.myAtoi('--1'), 0)
        self.assertEqual(self.s.myAtoi('-13+8'), -13)

    def test_longestCommonPrefix(self):
        self.assertEqual(self.s.longestCommonPrefix(["ff","ffc"]),"ff")
        self.assertEqual(self.s.longestCommonPrefix(["", ""]), "")
        self.assertEqual(self.s.longestCommonPrefix(["cca", "cca"]), "cca")
        self.assertEqual(self.s.longestCommonPrefix(["cca"]), 'cca')
        self.assertEqual(self.s.longestCommonPrefix(["flower", "flow", "flight"]), 'fl')
        self.assertEqual(self.s.longestCommonPrefix(["bab", "bcc"]), 'b')

    def test_new_longestCommonPrefix(self):
        self.assertEqual(self.s.new_longestCommonPrefix(["zzz","bbc","aaaa"]), '')



if __name__ == '__main__':
    unittest.main()