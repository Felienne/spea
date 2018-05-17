# 
class AboutAssignments(unittest.TestCase):
    def test_del_can_remove_entire_lists(self):
        lottery_nums = [4, 8, 15, 16, 23, 42]
        del lottery_nums

        with self.assertRaises(___): win = lottery_nums