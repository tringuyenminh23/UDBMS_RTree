import copy

from tests.test_case import TestCaseCompare
from tldb.core.structure.context import RangeContext
from tldb.core.structure.interval import Interval


class TestRangeContext(TestCaseCompare):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(test_path='core/structure/context/range_context')

    def test_str(self):
        method_name = self.id().split('.')[-1]
        context = RangeContext(['A', 'B', 'D'],
                               [Interval([6.0, 118.0]), Interval([17.0, 600.0]), Interval([13.0, 72.0])])
        with self.out_file[method_name].open(mode='w') as f:
            f.write(str(context))
        self.file_compare(self.out_file[method_name], self.exp_file[method_name])

    def test_check_intersection(self):
        context = RangeContext(['A', 'B', 'D'],
                               [Interval((6.0, 118.0)), Interval([17.0, 600.0]), Interval([13.0, 72.0])])

        res = context.check_intersection_and_update_boundaries(RangeContext(['A'], [Interval([100, 120])]))
        self.assertTrue(res)
        self.assertEqual(context.intervals, (Interval([100, 118]), Interval([17.0, 600.0]), Interval([13.0, 72.0])))

    def test_check_no_intersection(self):
        context = RangeContext(['A', 'B', 'D'],
                               [Interval([6.0, 118.0]), Interval([17.0, 600.0]), Interval([13.0, 72.0])])
        res = context.check_intersection_and_update_boundaries(RangeContext(['A'], [Interval([120, 130])]))
        self.assertFalse(res)
        self.assertEqual(context.intervals, (Interval([6.0, 118.0]), Interval([17.0, 600.0]), Interval([13.0, 72.0])))

    def test_check_multi_intersection(self):
        context = RangeContext(['A', 'B', 'D'],
                               [Interval([6.0, 118.0]), Interval([17.0, 600.0]), Interval([13.0, 72.0])])
        res = context.check_intersection_and_update_boundaries(
            RangeContext(['A', 'B'], [Interval([100, 120]), Interval([20, 30])]))
        self.assertTrue(res)
        self.assertEqual(context.intervals, (Interval([100, 118.0]), Interval([20, 30]), Interval([13.0, 72.0])))

    def test_check_one_failed_intersection(self):
        context = RangeContext(['A', 'B', 'D'],
                               [Interval([6.0, 118.0]), Interval([17.0, 600.0]), Interval([13.0, 72.0])])
        res = context.check_intersection_and_update_boundaries(
            RangeContext(['A', 'B'], [Interval([100, 120]), Interval([10, 15])]))
        self.assertFalse(res)
        self.assertEqual(context.intervals, (Interval([6.0, 118.0]), Interval([17.0, 600.0]), Interval([13.0, 72.0])))

    def test_copy(self):
        context1 = RangeContext(['A', 'B', 'D'],
                                [Interval([6.0, 118.0]), Interval([17.0, 600.0]), Interval([13.0, 72.0])])
        context2 = copy.copy(context1)
        context1.check_intersection_and_update_boundaries(
            RangeContext(['A', 'B'], [Interval([100, 120]), Interval([20, 30])]))
        self.assertNotEqual(context1, context2)
