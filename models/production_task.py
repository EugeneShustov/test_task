from odoo import models, fields, api
from datetime import datetime

class ProductionTask(models.Model):
    _name = 'production.task'
    _description = 'Задание на производство'

    name = fields.Char(string='Название', required=True)

    status = fields.Selection([
        ('ready', 'Готово к работе'),
        ('in_progress', 'В работе'),
        ('done', 'Готово'),
        ('rejected', 'Брак')
    ], string='Статус', default='ready')

    start_time = fields.Datetime(string='Время начала')
    end_time = fields.Datetime(string='Время окончания')
    operator_id = fields.Many2one('res.users', string='Оператор')

@api.model
def take_in_work(self, task_id):
    task = self.browse(task_id)
    task.status = 'in_progress'
    task.start_time = datetime.now()

@api.model
def mark_done(self, task_id):
    task = self.browse(task_id)
    task.status = 'done'
    task.end_time = datetime.now()

@api.model
def mark_rejected(self, task_id):
    task = self.browse(task_id)
    task.status = 'rejected'
    task.end_time = datetime.now()

