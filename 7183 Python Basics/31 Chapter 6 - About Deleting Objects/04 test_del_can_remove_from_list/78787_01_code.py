# 
class AboutAssignments(unittest.TestCase):
    def test_del_can_remove_from_list(self):
        lottery_nums = [4, 8, 15, 16, 23, 42]
        del lottery_nums[1]
        del lottery_nums[2:4]

        self.assertEqual(___, lottery_nums)