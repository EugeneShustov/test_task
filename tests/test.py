from odoo.tests.common import TransactionCase

class TestOperator(TransactionCase):
    def test_in_work(self):
        test = self.env['task'].create({'name': 'Задание'})
        test.test_in_work(task.id)
        self.assertEqual(task.status, 'in_progress')
        self.assertIsNotNone(task.start_time)
        